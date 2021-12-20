from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from constants import *
from pageObjects import *

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://blog.noveogroup.ru/")
driver.implicitly_wait(2)
driver.maximize_window()

main_page = SearchHelper(driver)
main_page.enter_search(search)
main_page.select_article()
assert exceptedText.lower() in main_page.find_text().lower()

driver.close()
