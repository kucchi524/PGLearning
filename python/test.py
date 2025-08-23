#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Web Scraping Tool with Selenium and Login Support
OBCログインページ対応スクレイピングツール（Selenium版）

Required packages:
pip install requests beautifulsoup4 lxml selenium webdriver-manager

Usage:
    python web_scraper_selenium.py
"""

import requests
from bs4 import BeautifulSoup
import csv
import json
import time
import random
from urllib.parse import urljoin, urlparse
from typing import List, Dict, Optional, Tuple, Union
import logging
import re
import os
from datetime import datetime
from env import OCB_ID, PASSWORD

# Selenium imports
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import (
    TimeoutException, NoSuchElementException, 
    ElementClickInterceptedException, WebDriverException
)
from webdriver_manager.chrome import ChromeDriverManager


class WebScraperSelenium:
    """
    Selenium対応ログイン機能付きWebスクレイピングツール
    """
    
    def __init__(self, delay_range=(1, 3), headless=True, headers=None):
        """
        Webスクレイピングツール（Selenium版）
        
        Args:
            delay_range: リクエスト間の待機時間（秒）の範囲
            headless: ヘッドレスモードでの実行
            headers: HTTPヘッダー
        """
        self.delay_range = delay_range
        self.headless = headless
        self.driver = None
        
        # requests session（非JavaScript用）
        self.session = requests.Session()
        default_headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        if headers:
            default_headers.update(headers)
        self.session.headers.update(default_headers)
        
        # ログ設定
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def init_driver(self):
        """
        Seleniumドライバーを初期化
        """
        if self.driver:
            return
        
        try:
            # Chrome オプション設定
            chrome_options = Options()
            if self.headless:
                chrome_options.add_argument("--headless")
            chrome_options.add_argument("--no-sandbox")
            chrome_options.add_argument("--disable-dev-shm-usage")
            chrome_options.add_argument("--disable-gpu")
            chrome_options.add_argument("--window-size=1920,1080")
            
            # User-Agent設定
            chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
            
            # ChromeDriverの自動管理
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service, options=chrome_options)
            
            # 暗黙的待機時間を設定
            self.driver.implicitly_wait(10)
            
            self.logger.info("Selenium WebDriver initialized successfully")
            
        except Exception as e:
            self.logger.error(f"Failed to initialize WebDriver: {e}")
            raise
    
    def close_driver(self):
        """
        Seleniumドライバーを終了
        """
        if self.driver:
            self.driver.quit()
            self.driver = None
            self.logger.info("WebDriver closed")
    
    def get_page_selenium(self, url: str, wait_time: int = 10) -> Optional[BeautifulSoup]:
        """
        Seleniumでページを取得してBeautifulSoupオブジェクトを返す
        
        Args:
            url: 取得するURL
            wait_time: ページ読み込み待機時間
            
        Returns:
            BeautifulSoupオブジェクト または None
        """
        try:
            if not self.driver:
                self.init_driver()
            
            self.driver.get(url)
            
            # ページの読み込み完了を待機
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            # BeautifulSoupオブジェクトを作成
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            self.logger.info(f"Successfully fetched with Selenium: {url}")
            return soup
            
        except TimeoutException:
            self.logger.error(f"Timeout waiting for page to load: {url}")
            return None
        except Exception as e:
            self.logger.error(f"Error fetching {url} with Selenium: {e}")
            return None
    
    def click_element_by_xpath(self, xpath: str, wait_time: int = 10) -> bool:
        """
        XPathで指定した要素をクリック
        
        Args:
            xpath: クリック対象要素のXPath
            wait_time: 要素の出現待機時間
            
        Returns:
            クリック成功可否
        """
        try:
            if not self.driver:
                self.init_driver()
            
            # 要素が表示されるまで待機
            element = WebDriverWait(self.driver, wait_time).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            
            # JavaScript経由でクリック（より確実）
            self.driver.execute_script("arguments[0].click();", element)
            
            self.logger.info(f"Successfully clicked element: {xpath}")
            time.sleep(1)  # クリック後の待機
            return True
            
        except TimeoutException:
            self.logger.error(f"Timeout waiting for clickable element: {xpath}")
            return False
        except ElementClickInterceptedException:
            self.logger.error(f"Element click intercepted: {xpath}")
            # 通常のクリックを試行
            try:
                element = self.driver.find_element(By.XPATH, xpath)
                element.click()
                return True
            except:
                return False
        except Exception as e:
            self.logger.error(f"Error clicking element {xpath}: {e}")
            return False
    
    def wait_for_element(self, xpath: str, wait_time: int = 10) -> bool:
        """
        XPathで指定した要素の出現を待機
        
        Args:
            xpath: 待機対象要素のXPath
            wait_time: 待機時間
            
        Returns:
            要素発見可否
        """
        try:
            if not self.driver:
                self.init_driver()
                
            WebDriverWait(self.driver, wait_time).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            self.logger.info(f"Element found: {xpath}")
            return True
        except TimeoutException:
            self.logger.error(f"Timeout waiting for element: {xpath}")
            return False
    
    def login_obc_selenium(self, login_url: str, obc_id: str, password: str) -> bool:
        """
        SeleniumでOBCログインページにログイン
        
        Args:
            login_url: ログインページのURL
            obc_id: OBCiD
            password: パスワード
            
        Returns:
            ログイン成功可否
        """
        try:
            if not self.driver:
                self.init_driver()
            
            # ログインページに移動
            self.driver.get(login_url)
            
            # ログインフォームの要素を探す
            # OBCiD入力フィールド
            id_selectors = [
                "input[name*='id']", "input[name*='user']", "input[name*='login']",
                "input[id*='id']", "input[id*='user']", "input[id*='login']",
                "input[type='text']", "input[type='email']"
            ]
            
            # パスワード入力フィールド
            password_selectors = [
                "input[name*='password']", "input[name*='passwd']",
                "input[id*='password']", "input[id*='passwd']",
                "input[type='password']"
            ]
            
            # OBCiD入力
            id_field = None
            for selector in id_selectors:
                try:
                    id_field = self.driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except NoSuchElementException:
                    continue
            
            if not id_field:
                self.logger.error("Could not find ID input field")
                return False
            
            id_field.clear()
            id_field.send_keys(obc_id)
            self.logger.info("OBC ID entered")
            
            # パスワード入力
            password_field = None
            for selector in password_selectors:
                try:
                    password_field = self.driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except NoSuchElementException:
                    continue
            
            if not password_field:
                self.logger.error("Could not find password input field")
                return False
            
            password_field.clear()
            password_field.send_keys(password)
            self.logger.info("Password entered")
            
            # 認証方法でパスワード認証を選択（存在する場合）
            try:
                auth_radio = self.driver.find_element(By.CSS_SELECTOR, "input[value*='password']")
                if not auth_radio.is_selected():
                    auth_radio.click()
            except NoSuchElementException:
                pass  # 認証方法選択がない場合は無視
            
            # ログインボタンをクリック
            login_button_selectors = [
                "input[type='submit']", "button[type='submit']",
                "input[value*='ログイン']", "button[class*='login']",
                "input[value*='Login']", "button[class*='Login']"
            ]
            
            login_button = None
            for selector in login_button_selectors:
                try:
                    login_button = self.driver.find_element(By.CSS_SELECTOR, selector)
                    break
                except NoSuchElementException:
                    continue
            
            if not login_button:
                self.logger.error("Could not find login button")
                return False
            
            login_button.click()
            self.logger.info("Login button clicked")
            
            # ログイン成功の確認（URLの変化またはダッシュボード要素の表示を待機）
            time.sleep(3)
            current_url = self.driver.current_url
            
            if current_url != login_url or 'dashboard' in current_url.lower():
                self.logger.info("Login successful")
                return True
            else:
                # エラーメッセージの確認
                page_text = self.driver.page_source.lower()
                error_indicators = [
                    'error', 'エラー', 'invalid', '無効', 'failed', '失敗',
                    'incorrect', '間違い', 'wrong', 'パスワードが'
                ]
                
                if any(indicator in page_text for indicator in error_indicators):
                    self.logger.error("Login failed - error message detected")
                    return False
                
                self.logger.info("Login appears successful")
                return True
            
        except Exception as e:
            self.logger.error(f"Login error: {e}")
            return False
    
    def scrape_with_clicks(self, login_url: str, obc_id: str, password: str,
                          click_sequence: List[Dict], selectors: Dict[str, str]) -> List[Dict[str, any]]:
        """
        ログイン後にクリック操作を含むスクレイピングを実行
        
        Args:
            login_url: ログインページURL
            obc_id: OBCiD
            password: パスワード
            click_sequence: クリック操作のシーケンス
            selectors: データ抽出用CSSセレクター
            
        Returns:
            抽出データのリスト
        """
        try:
            # ログイン実行
            if not self.login_obc_selenium(login_url, obc_id, password):
                self.logger.error("Login failed, cannot proceed with scraping")
                return []
            
            results = []
            
            for i, click_info in enumerate(click_sequence, 1):
                self.logger.info(f"Processing click sequence {i}/{len(click_sequence)}")
                
                # ページに移動（必要な場合）
                if 'url' in click_info:
                    self.driver.get(click_info['url'])
                    time.sleep(2)
                
                # クリック前のデータ取得（必要な場合）
                if click_info.get('scrape_before', False):
                    soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                    data = {'step': f'before_click_{i}'}
                    for field, selector in selectors.items():
                        elements = soup.select(selector)
                        data[field] = [elem.get_text(strip=True) for elem in elements]
                    results.append(data)
                
                # 要素をクリック
                if 'xpath' in click_info:
                    if not self.click_element_by_xpath(click_info['xpath']):
                        self.logger.warning(f"Failed to click element: {click_info['xpath']}")
                        continue
                
                # クリック後の待機
                wait_time = click_info.get('wait_after', 2)
                time.sleep(wait_time)
                
                # クリック後のデータ取得
                soup = BeautifulSoup(self.driver.page_source, 'html.parser')
                data = {
                    'step': f'after_click_{i}',
                    'url': self.driver.current_url,
                    'timestamp': datetime.now().isoformat()
                }
                
                for field, selector in selectors.items():
                    elements = soup.select(selector)
                    data[field] = [elem.get_text(strip=True) for elem in elements]
                
                results.append(data)
                
                # 次の操作まで待機
                if i < len(click_sequence):
                    delay = random.uniform(*self.delay_range)
                    time.sleep(delay)
            
            return results
            
        except Exception as e:
            self.logger.error(f"Error in scrape_with_clicks: {e}")
            return []
        finally:
            self.close_driver()
    
    def extract_text(self, soup: BeautifulSoup, selector: str) -> List[str]:
        """
        CSSセレクターを使ってテキストを抽出
        """
        elements = soup.select(selector)
        return [elem.get_text(strip=True) for elem in elements]
    
    def save_to_csv(self, data: List[Dict], filename: str):
        """
        データをCSVファイルに保存
        """
        if not data:
            self.logger.warning("No data to save")
            return
        
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name, ext = os.path.splitext(filename)
        filename_with_timestamp = f"{base_name}_{timestamp}{ext}"
        
        # すべてのキーを取得
        all_keys = set()
        for item in data:
            all_keys.update(item.keys())
        
        with open(filename_with_timestamp, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(all_keys))
            writer.writeheader()
            
            for item in data:
                # リスト値を文字列に変換
                row = {}
                for key, value in item.items():
                    if isinstance(value, list):
                        row[key] = ' | '.join(str(v) for v in value)
                    else:
                        row[key] = str(value)
                writer.writerow(row)
        
        self.logger.info(f"Data saved to {filename_with_timestamp}")
    
    def save_to_json(self, data: List[Dict], filename: str):
        """
        データをJSONファイルに保存
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        base_name, ext = os.path.splitext(filename)
        filename_with_timestamp = f"{base_name}_{timestamp}{ext}"
        
        with open(filename_with_timestamp, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        
        self.logger.info(f"Data saved to {filename_with_timestamp}")


def main():
    """
    メイン関数 - 使用例とテスト
    """
    # スクレイパーのインスタンスを作成（ヘッドレスモード）
    scraper = WebScraperSelenium(delay_range=(2, 4), headless=True)
    
    # 環境変数から認証情報を取得
    obc_id = OCB_ID
    password = PASSWORD
    
    if not obc_id or not password:
        print("認証情報が設定されていません。")
        print("以下のコマンドで環境変数を設定してください:")
        print("export OBC_ID='your_obc_id'")
        print("export OBC_PASSWORD='your_password'")
        return
    
    print(f"認証情報確認: OBC_ID = {obc_id}")
    
    # OBCログイン付きクリック操作スクレイピングの例
    login_url = "https://id.obc.jp/b95ol0qzdq12/?manuallogin=True"
    
    # クリック操作のシーケンス
    click_sequence = [
        {
            'url': 'https://example.obc.jp/statements',  # 実際のURLに置き換え
            'xpath': '//*[@id="js-payStatementTable"]/tbody/tr[1]/td[2]/span[1]',  # 提供されたXPath
            'wait_after': 3,  # クリック後の待機時間（秒）
            'scrape_before': False  # クリック前にもデータを取得するか
        },
        # 必要に応じて追加のクリック操作
        # {
        #     'xpath': '//*[@id="next-button"]',
        #     'wait_after': 2
        # }
    ]
    
    # データ抽出用セレクター
    selectors = {
        'page_title': 'h1, .page-title, .title',
        'statements': '.statement-item, .pay-statement, tr',
        'amounts': '.amount, .price, .value',
        'dates': '.date, .pay-date, .statement-date',
        'details': '.detail, .description, p'
    }
    
    print("=== ログイン付きクリック操作スクレイピング開始 ===")
    
    try:
        results = scraper.scrape_with_clicks(
            login_url=login_url,
            obc_id=obc_id,
            password=password,
            click_sequence=click_sequence,
            selectors=selectors
        )
        
        if results:
            print(f"データ抽出完了: {len(results)} ステップ")
            
            # データ保存
            scraper.save_to_csv(results, 'obc_click_scraping.csv')
            scraper.save_to_json(results, 'obc_click_scraping.json')
            
            # 結果の一部を表示
            for i, result in enumerate(results):
                print(f"\n--- ステップ {i+1} ---")
                print(f"URL: {result.get('url', 'N/A')}")
                print(f"タイムスタンプ: {result.get('timestamp', 'N/A')}")
                for key, value in result.items():
                    if key not in ['url', 'timestamp', 'step'] and value:
                        print(f"{key}: {value[:2] if isinstance(value, list) else str(value)[:100]}...")
        else:
            print("データの抽出に失敗しました")
            
    except Exception as e:
        print(f"エラーが発生しました: {e}")
    finally:
        scraper.close_driver()
    
    print("スクレイピング処理が完了しました。")


if __name__ == "__main__":
    main()