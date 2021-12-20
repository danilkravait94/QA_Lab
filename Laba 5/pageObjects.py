from basePage import BasePage
from selenium.webdriver.common.keys import Keys

class SearchHelper(BasePage):

    def enter_search(self, text):
        search_field = self.driver.find_element_by_css_selector("[type=search]")
        search_field.send_keys(text, Keys.ENTER)
        return search_field

    def select_article(self):
        self.driver.find_element_by_tag_name("article").click()

    def find_text(self):
        return self.driver.find_element_by_css_selector("article>header>h2").text
