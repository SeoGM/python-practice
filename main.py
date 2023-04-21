
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import  ActionChains

driver = webdriver.Chrome()
url = 'https://sir.kr'
driver.get(url)            # url 오픈해라
driver.maximize_window()   #창 크게 만들기
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()
url = 'https://sir.kr'
driver.get(url)            # url 오픈해라
driver.maximize_window()  # 창 크게 만들기
