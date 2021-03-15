
from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import time
import csv
import os
import pandas as pd
import numpy as np

# get yahoo login informaiton
with open('../../login_info/yahoo.csv') as f:
    user_name_yahoo, login_password_yahoo = f.read().split(",")

# login to yahoo
browser = webdriver.Chrome()
url_login = "https://login.yahoo.co.jp/config/login"
browser.get(url_login)
browser.find_element_by_id('username').send_keys(user_name_yahoo)
time.sleep(2)
browser.find_element_by_id('btnNext').click()
time.sleep(2)
browser.find_element_by_id('passwd').send_keys(login_password_yahoo)
time.sleep(2)
browser.find_element_by_id('btnSubmit').click()
time.sleep(3)

# download file from yahoo
ID_list = list(pd.read_csv('../list/stock_list.csv')['code'].astype(str).map(str) + ('.T'))
print(ID_list)

for ID in ID_list:
    url_csvfile = "https://download.finance.yahoo.co.jp/common/history/{security_code}.csv".format(security_code=ID)
    print(url_csvfile)
    browser.get(url_csvfile)
    time.sleep(np.random.rand()*10)
