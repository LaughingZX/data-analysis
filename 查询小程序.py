#coding = "utf8"
import win32api
import os
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

path1 = "C:\\Users\\Administrator\\Desktop\\AAA.csv"
path2 = "C:\\Users\\Administrator\\Desktop\\sales.xlsx"

'''if os.path.exists(path):
    #win32api.ShellExecute(0, 'open', 'http://www.sohu.com', '', '', 1)'''

condition = input('please enter one condition: ')

def search_pro(condition):
    pattern_one = r'.*AA.*'
    pattern_two = r'.*sale.*'
    pattern_three = r'.*sohu.*'
    pattern_four = r'.*baidu.*'
    if re.search(pattern_one,condition):
        win32api.ShellExecute(0,"open",path1,"","",1)
    elif re.search(pattern_two,condition):
        win32api.ShellExecute(0,"open",path2,"","",1)
    elif re.search(pattern_three,condition):
        win32api.ShellExecute(0, 'open', 'https://www.sohu.com', '', '', 1)
    elif re.search(pattern_four,condition):
        browser = webdriver.Chrome()
        browser.get("https://baidu.com/")
        inputs = browser.find_element_by_id('kw')
        inputs.send_keys("github")
        inputs.send_keys(Keys.ENTER)
        wait = WebDriverWait(browser,10)
        wait.until(EC.presence_of_element_located((By.ID,"page")))
        print(browser.current_url)
        time.sleep(1800)
    else:
        print("no result!")
    
search_pro(condition)
