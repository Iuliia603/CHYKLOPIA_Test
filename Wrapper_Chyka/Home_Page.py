from CHYKALOPIA.Wrapper_Chyka.Header import Header
from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By

class HomePage:
    def __init__(self, browser):
        self.header = Header(browser)

        self.homepage_title = Element(browser, By.XPATH, '//*[@id="content"]/div/div[1]/section[1]/div[2]/div[1]/div/div[1]/div/p')

    def get_homepage_title(self):
        return self.get_homepage_title().get_text()

