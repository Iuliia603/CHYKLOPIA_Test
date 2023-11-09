from CHYKALOPIA.Wrapper_Chyka.Header import Header
from CHYKALOPIA.Wrapper_Chyka.Home_Page import HomePage
from CHYKALOPIA.Wrapper_Chyka.UIElement import UIElement as Element
from selenium.webdriver.common.by import By


class WorkPage:
    def __init__(self, browser):
        self.header = Header(browser)
        self.homepage = HomePage(browser)

        self.work_title = Element(browser, By.XPATH,'//*[@id="content"]/div/div[1]/section[1]/div[2]/div[1]/div/div[2]/div/p')

    def get_work_title (self):
        return self.work_title.get_text()