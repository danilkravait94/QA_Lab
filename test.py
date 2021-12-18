from time import sleep
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from constants import *

driver = webdriver.Chrome(path)
driver.maximize_window()
driver.implicitly_wait(3)

driver.get("https://blog.noveogroup.ru/")

sleep(1)
driver.find_element_by_css_selector("[type=search]").send_keys(search)
sleep(1)
driver.find_element_by_css_selector("[type=search]").send_keys(Keys.ENTER)

sleep(1)
driver.find_element_by_tag_name("article").click()

sleep(1)
title = driver.find_element_by_css_selector("article>header>h2").text
assert title == "Как тестировщику войти в проект так, чтобы все и всем было хорошо", "Fail fail fail"
print("Yeah! That's it!")

sleep(5)
driver.close()