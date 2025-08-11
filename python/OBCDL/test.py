import time
import os
from selenium import webdriver as wd
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from env import LOGIN_URL, OBC_ID, PASSWORD, DL_DIR, STATEMENT_XPATH, D_PATH

downloadDir = DL_DIR
saveDir = D_PATH

# chromeを起動してOBCIDにアクセス    
driver = wd.Chrome()
driver.get(LOGIN_URL)
time.sleep(2)

# ログインIDを入力
idElement = driver.find_element(By.ID, "OBCID").send_keys(OBC_ID)
time.sleep(1)
driver.find_element(By.ID, "checkAuthPolisyBtn").click()
time.sleep(3)

# パスワードを入力して認証
passElement = driver.find_element(By.ID, "Password").send_keys(PASSWORD)
time.sleep(1)
driver.find_element(By.ID, "login").click()
time.sleep(5)

statementElement = driver.find_element(By.XPATH, STATEMENT_XPATH).click()
time.sleep(3)

