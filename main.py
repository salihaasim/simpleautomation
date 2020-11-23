from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd


chromedriver_path ='C:\\chrome driver\\chromedriver_win32\\chromedriver.exe' # Change this to your own chromedriver path!
webdriver = webdriver.Chrome(chromedriver_path)
sleep(1)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(2)
username = webdriver.find_element_by_name('username')
username.send_keys('username')#Change this to your own Instagram username
password = webdriver.find_element_by_name('password')
password.send_keys('password') # Change this to your own Instagram password

button_login = webdriver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]/button/div')
button_login.click()
sleep(3)
try:
    notnow = webdriver.find_element_by_xpath('/html/body/div[4]/div/div/div/div[3]/button[2]')
    notnow.click() # Comment these last 2 lines out, if you don't get a pop up asking about notifications
except :
    pass
search = webdriver.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.send_keys('irfan view')