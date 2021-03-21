import datetime
import shutil
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
import os
import pandas as pd
import numpy as np



def init_driver():
    download_directory_path = os.path.abspath(os.getcwd() + "/../../download_tmp/")
    options_chrome = webdriver.ChromeOptions()
    prefs = {"download.default_directory": download_directory_path}
    options_chrome.add_experimental_option("prefs", prefs)
    driver = webdriver.Chrome(options=options_chrome)
    return driver


# login to yahoo
def login_yahoo(driver):
    with open('../../login_info/yahoo.csv') as f:
        user_name_yahoo, login_password_yahoo = f.read().split(",")
    url_login = "https://login.yahoo.co.jp/config/login"
    driver.get(url_login)
    driver.find_element_by_id('username').send_keys(user_name_yahoo)
    time.sleep(2)
    driver.find_element_by_id('btnNext').click()
    time.sleep(2)
    driver.find_element_by_id('passwd').send_keys(login_password_yahoo)
    time.sleep(2)
    driver.find_element_by_id('btnSubmit').click()
    time.sleep(3)


def get_data(driver):
    id_list = list(pd.read_csv('../list/stock_list.csv')['code'].astype(str).map(str) + ('.T'))
    for ID in id_list:
        url_csvfile = "https://download.finance.yahoo.co.jp/common/history/{security_code}.csv".format(security_code=ID)
        print(url_csvfile)
        driver.get(url_csvfile)
        time.sleep(np.random.rand() * 10 + 1)

def backup_old_data():
    download_directory_path = os.path.abspath(os.getcwd() + "/../../download_tmp/")
    backup_dir= download_directory_path + '/' + datetime.date.today().strftime("%Y%m%d")
    try:
        os.makedirs(backup_dir, exist_ok=True)
    except:
        pass

    for file_name in os.listdir(download_directory_path):
        file = download_directory_path + '/' + file_name
        shutil.move(file, backup_dir)



def main():
    backup_old_data()
    driver = init_driver()
    login_yahoo(driver)
    get_data(driver)
    driver.quit()

if __name__ == "__main__":
    main()

