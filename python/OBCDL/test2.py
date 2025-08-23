import time
import os
import shutil
from datetime import datetime
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from env import LOGIN_URL, OBC_ID, PASSWORD, D_PATH

def setup_download_preferences():
    """ダウンロード設定付きでChromeを起動"""
    download_path = D_PATH
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    options = wd.ChromeOptions()
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "plugins.always_open_pdf_externally": True
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option('useAutomationExtension', False)

    driver = wd.Chrome(options=options)
    driver.maximize_window()
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")

    return driver, download_path

def login_to_obc(driver):
    """OBCにログイン"""
    try:
        print("OBCにログイン中...")
        driver.get(LOGIN_URL)

        wait = WebDriverWait(driver, 20)
        wait.until(EC.presence_of_element_located((By.ID, "loginform")))
        time.sleep(3)

        page_state = driver.execute_script("""
        return {
            isPasswordView: $('#js-inputPasswordView').is(':visible'),
            currentOBCID: $('#js-om-selectedOBCID').val() || ''
        };
        """)

        if not page_state['isPasswordView'] or page_state['currentOBCID'] != OBC_ID:
            try:
                obcid_field = driver.find_element(By.ID, "OBCID")
                obcid_field.clear()
                obcid_field.send_keys(OBC_ID)
                next_button = driver.find_element(By.CLASS_NAME, "js-loginNextButton")
                next_button.click()
                time.sleep(3)
            except:
                try:
                    id_elements = driver.find_elements(By.CLASS_NAME, "js-selectID")
                    for element in id_elements:
                        if OBC_ID in element.text:
                            element.click()
                            time.sleep(3)
                            break
                except:
                    print("OBCIDの設定をスキップします")

        password_field = wait.until(EC.element_to_be_clickable((By.ID, "Password")))
        password_field.clear()
        password_field.send_keys(PASSWORD)
        time.sleep(1)

        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
        login_button.click()
        time.sleep(5)

        if "login" not in driver.current_url.lower():
            print("✅ ログイン成功")
            return True
        else:
            print("❌ ログインに失敗した可能性があります")
            return False
    except Exception as e:
        print(f"❌ ログインエラー: {e}")
        return False

def navigate_to_payslip_page(driver):
    """給与明細ページに移動"""
    try:
        wait = WebDriverWait(driver, 15)
        print("給与明細ページを探しています...")

        tables = driver.find_elements(By.CLASS_NAME, "p-payStatementTable__tbody")
        if tables:
            print("✅ 給与明細テーブルを発見")
            return True

        pay_elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'pay') or contains(@class, 'salary') or contains(@class, 'statement')]")
        if pay_elements:
            print("✅ 給与関連の要素を発見")
            return True

        print("⚠️ 給与明細ページが見つかりません")
        return False
    except Exception as e:
        print(f"❌ ページナビゲーションエラー: {e}")
        return False

def download_payslip_by_row_index(driver, download_path, row_index=2):
    """
    給与明細テーブルの上から row_index 行目をクリックしてDLする
    デフォルト: 上から3行目（row_index=2）
    """
    try:
        wait = WebDriverWait(driver, 15)
        print("給与明細テーブルを探しています...")

        tbody = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "p-payStatementTable__tbody")))
        all_rows = tbody.find_elements(By.CSS_SELECTOR, "tr")

        candidate_rows = []
        for r in all_rows:
            cls = (r.get_attribute("class") or "")
            if "js-cm-webIO__fileDownload" in cls or "tr-payStatement" in cls:
                candidate_rows.append(r)
        rows = candidate_rows if candidate_rows else all_rows

        if not rows or len(rows) <= row_index:
            print(f"❌ 対象行が見つかりません（取得行数: {len(rows)} / 要求: {row_index+1}行目）")
            return False

        target_row = rows[row_index]
        driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", target_row)
        time.sleep(0.5)
        try:
            target_row.click()
        except:
            driver.execute_script("arguments[0].click();", target_row)

        initial_files = set(os.listdir(download_path)) if os.path.exists(download_path) else set()
        print("ダウンロード完了を待機中...")
        max_wait_time, wait_interval = 30, 1

        for i in range(max_wait_time):
            time.sleep(wait_interval)
            current_files = set(os.listdir(download_path))
            new_files = current_files - initial_files
            completed = [f for f in new_files if not f.endswith(".crdownload")]
            if completed:
                print(f"✅ ダウンロード完了: {completed}")
                return True
            if i % 5 == 0:
                print(f"ダウンロード待機中... ({i}/{max_wait_time}秒)")

        print("⚠️ ダウンロード完了を確認できませんでした")
        return False
    except Exception as e:
        print(f"❌ ダウンロードエラー: {e}")
        return False

def move_and_rename_file(download_path, target_path):
    """
    最新のダウンロードファイルを <target_path>/<year>/ に移動し、
    yyyymm へリネーム。ファイル名が末尾 "S.pdf" のときは "yyyymm賞与.pdf" にする。
    例:
      (000472)202506S.pdf -> 202506賞与.pdf
      (000472)202507.pdf  -> 202507.pdf
      (000472)202507K.pdf -> 202507.pdf
    """
    os.makedirs(target_path, exist_ok=True)

    # .crdownload を除外した最新ファイルを特定
    files = [f for f in os.listdir(download_path) if not f.endswith(".crdownload")]
    if not files:
        print("❌ 移動対象ファイルが見つかりません")
        return False

    latest_file = max([os.path.join(download_path, f) for f in files], key=os.path.getctime)
    filename = os.path.basename(latest_file)
    ext = os.path.splitext(filename)[1]          # 例: ".pdf"
    name_upper = filename.upper()                # 大文字化して安全に比較

    # yyyymm と year は保存名/保存先用（ダウンロード日ベース）
    yyyymm = datetime.now().strftime("%Y%m")
    year = datetime.now().strftime("%Y")

    # ファイル名末尾が "S.pdf" なら賞与
    if name_upper.endswith("S.PDF"):
        new_filename = f"{yyyymm}賞与{ext}"
    else:
        new_filename = f"{yyyymm}{ext}"

    save_dir = os.path.join(target_path, year)
    os.makedirs(save_dir, exist_ok=True)

    new_path = os.path.join(save_dir, new_filename)
    shutil.move(latest_file, new_path)
    print(f"✅ ファイルを移動＆リネームしました: {new_path}")
    return True

def main():
    print("=== OBC給与明細ダウンロード ===")
    driver, download_path = setup_download_preferences()
    print(f"ダウンロードフォルダ: {download_path}")

    try:
        if not login_to_obc(driver):
            return

        if not navigate_to_payslip_page(driver):
            print("⚠️ 給与明細ページへの移動をスキップ")

        # 上から3行目をダウンロード
        if download_payslip_by_row_index(driver, download_path, row_index=2):
            move_and_rename_file(download_path, D_PATH)
            print("✅ 処理完了")
        else:
            print("❌ ダウンロードに失敗しました")

    except Exception as e:
        print(f"❌ 予期しないエラー: {e}")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
