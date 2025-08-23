import time
import os
import shutil
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from env import LOGIN_URL, OBC_ID, PASSWORD, D_PATH

def setup_download_preferences():
    """ダウンロード設定付きでChromeを起動"""
    
    # ダウンロードフォルダを指定
    download_path = D_PATH
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    options = wd.ChromeOptions()
    
    # ダウンロード設定
    prefs = {
        "download.default_directory": download_path,
        "download.prompt_for_download": False,
        "download.directory_upgrade": True,
        "safebrowsing.enabled": True,
        "plugins.always_open_pdf_externally": True  # PDFを外部で開く
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
        
        # パスワード画面が既に表示されているかチェック
        page_state = driver.execute_script("""
        return {
            isPasswordView: $('#js-inputPasswordView').is(':visible'),
            currentOBCID: $('#js-om-selectedOBCID').val() || ''
        };
        """)
        
        if not page_state['isPasswordView'] or page_state['currentOBCID'] != OBC_ID:
            # ID入力が必要な場合
            try:
                obcid_field = driver.find_element(By.ID, "OBCID")
                obcid_field.clear()
                obcid_field.send_keys(OBC_ID)
                
                next_button = driver.find_element(By.CLASS_NAME, "js-loginNextButton")
                next_button.click()
                time.sleep(3)
                
            except:
                # ID選択画面の場合
                try:
                    target_id_element = None
                    id_elements = driver.find_elements(By.CLASS_NAME, "js-selectID")
                    for element in id_elements:
                        if OBC_ID in element.text:
                            target_id_element = element
                            break
                    
                    if target_id_element:
                        target_id_element.click()
                        time.sleep(3)
                
                except:
                    print("OBCIDの設定をスキップします")
        
        # パスワード入力
        password_field = wait.until(EC.element_to_be_clickable((By.ID, "Password")))
        password_field.clear()
        password_field.send_keys(PASSWORD)
        time.sleep(1)
        
        # ログインボタンをクリック
        login_button = wait.until(EC.element_to_be_clickable((By.ID, "login")))
        login_button.click()
        
        print("ログイン処理完了を待機中...")
        time.sleep(5)
        
        # ログイン成功の確認
        current_url = driver.current_url
        if "login" not in current_url.lower():
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
        
        # 給与明細ページのリンクを探す
        print("給与明細ページを探しています...")
        
        # キューブボタンから給与明細ページへのリンクを踏む
        possible_links = ['//*[@id="js-cm-ptl-portalTabArea"]/div[1]/div[1]/div[1]/button',
                          '//*[@id="js-cm-ptl-serviceListPanel"]/div/a[1]/img']
        
        found_link = False
        
        for link_text in possible_links:
            try:
                # リンクテキストで探す
                links = driver.find_elements(By.PARTIAL_LINK_TEXT, link_text)
                if links:
                    print(f"'{link_text}'リンクを発見してクリック")
                    links[0].click()
                    time.sleep(3)
                    links[1].click()
                    time.sleep(3)
                    found_link = True
                    break
                
                # ボタンやナビゲーション要素で探す
                elements = driver.find_elements(By.XPATH, f"//*[contains(text(), '{link_text}')]")
                for element in elements:
                    if element.is_displayed() and element.is_enabled():
                        print(f"'{link_text}'要素を発見してクリック")
                        driver.execute_script("arguments[0].click();", element)
                        time.sleep(3)
                        found_link = True
                        break
                        
                if found_link:
                    break
                    
            except:
                continue
        
        if not found_link:
            print("⚠️ 給与明細ページへのリンクが見つかりません")
            print("現在のページで給与明細テーブルを探します...")
        
        # テーブルが既に表示されているかチェック
        tables = driver.find_elements(By.CLASS_NAME, "p-payStatementTable__tbody")
        if tables:
            print("✅ 給与明細テーブルを発見")
            return True
        
        # より広範囲で給与明細の要素を探す
        pay_elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'pay') or contains(@class, 'salary') or contains(@class, 'statement')]")
        if pay_elements:
            print("✅ 給与関連の要素を発見")
            return True
            
        return False
        
    except Exception as e:
        print(f"❌ ページナビゲーションエラー: {e}")
        return False

def download_top_payslip(driver, download_path):
    """一番上の給与明細をダウンロード"""
    
    try:
        wait = WebDriverWait(driver, 15)
        
        print("給与明細テーブルを探しています...")
        
        # まずテーブル全体を探す
        table_found = False
        
        # パターン1: tbody要素を直接探す
        try:
            tbody = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "p-payStatementTable__tbody")))
            print("✅ 給与明細テーブル(tbody)を発見")
            table_found = True
        except:
            print("tbody要素が見つかりません")
        
        if not table_found:
            # パターン2: より広範囲で探す
            try:
                table_elements = driver.find_elements(By.XPATH, "//*[contains(@class, 'payStatement') or contains(@class, 'pay-statement')]")
                if table_elements:
                    print("✅ 給与明細関連要素を発見")
                    table_found = True
            except:
                print("給与明細要素が見つかりません")
        
        if not table_found:
            print("❌ 給与明細テーブルが見つかりません")
            return False
        
        # 一番上の行を探す
        print("一番上の給与明細行を探しています...")
        
        # パターン1: 指定されたクラス名で探す
        try:
            top_row = driver.find_element(By.CSS_SELECTOR, "tr.js-cm-webIO__fileDownload.js-refP_actionLog.tr-payStatement")
            print("✅ 一番上の給与明細行を発見 (CSS selector)")
        except:
            # パターン2: data-key属性で探す（提供されたHTMLの最初の要素）
            try:
                top_row = driver.find_element(By.CSS_SELECTOR, "tr[data-key='322a9462-09ba-4c22-ae13-5eefc003cec2']")
                print("✅ 一番上の給与明細行を発見 (data-key)")
            except:
                # パターン3: クラス名のいずれかで探す
                try:
                    rows = driver.find_elements(By.CLASS_NAME, "js-cm-webIO__fileDownload")
                    if rows:
                        top_row = rows[0]  # 最初の行
                        print("✅ 一番上の給与明細行を発見 (class name)")
                    else:
                        raise Exception("行が見つかりません")
                except:
                    print("❌ 給与明細行が見つかりません")
                    return False
        
        # 行の内容を確認
        try:
            row_text = top_row.text
            print(f"対象行の内容: {row_text}")
        except:
            print("行の内容を取得できませんでした")
        
        # ダウンロード前のファイル数を確認
        initial_files = set(os.listdir(download_path)) if os.path.exists(download_path) else set()
        
        print("給与明細行をクリックしてダウンロード開始...")
        
        # スクロールして要素を表示
        driver.execute_script("arguments[0].scrollIntoView(true);", top_row)
        time.sleep(1)
        
        # クリック実行
        try:
            # まず通常のクリックを試す
            top_row.click()
            print("✅ 行をクリックしました")
        except:
            # JavaScriptクリックを試す
            driver.execute_script("arguments[0].click();", top_row)
            print("✅ 行をJavaScriptでクリックしました")
        
        # ダウンロード完了を待機
        print("ダウンロード完了を待機中...")
        
        max_wait_time = 30  # 最大30秒待機
        wait_interval = 1   # 1秒間隔でチェック
        
        for i in range(max_wait_time):
            time.sleep(wait_interval)
            
            if os.path.exists(download_path):
                current_files = set(os.listdir(download_path))
                new_files = current_files - initial_files
                
                if new_files:
                    # .crdownloadファイル（Chrome一時ファイル）を除外
                    completed_files = [f for f in new_files if not f.endswith('.crdownload')]
                    if completed_files:
                        print(f"✅ ダウンロード完了: {completed_files}")
                        return True
            
            if i % 5 == 0:  # 5秒ごとに進捗表示
                print(f"ダウンロード待機中... ({i}/{max_wait_time}秒)")
        
        print("⚠️ ダウンロード完了を確認できませんでした")
        return False
        
    except Exception as e:
        print(f"❌ ダウンロードエラー: {e}")
        return False

# ダウンロード後の処理を追加
def move_and_rename_file(download_path, target_path, year):
    """
    最新のダウンロードファイルを <target_path>/<year>/ に移動し、
    yyyymm へリネーム。ファイル名が末尾 "S.pdf" のときは "yyyymm賞与.pdf" にする。
    例:
      202506S.pdf -> 202506賞与.pdf
      202507.pdf  -> 202507.pdf
      202507K.pdf -> 202507.pdf
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
    """メイン処理"""
    
    print("=== OBC給与明細ダウンロード ===")
    year = datetime.now().strftime("%Y")
    
    # ダウンロード設定付きでブラウザを起動
    driver, download_path = setup_download_preferences()
        
    try:
        # ログイン
        if not login_to_obc(driver):
            print("❌ ログインに失敗しました")
            return
        
        # 給与明細ページに移動
        if not navigate_to_payslip_page(driver):
            print("⚠️ 給与明細ページへの移動をスキップ（現在のページで続行）")
        
        # トップの給与明細をダウンロード
        if download_top_payslip(driver, download_path):
            move_and_rename_file(download_path, D_PATH, year)
            print("✅ 処理完了")
        else:
            print("❌ ダウンロードに失敗しました")
        
        print(f"\nダウンロードフォルダを確認してください: {download_path + year}")
        
    except Exception as e:
        print(f"❌ 予期しないエラー: {e}")
    
    finally:
        driver.quit()

if __name__ == "__main__":
    main()