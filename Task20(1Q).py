from selenium import webdriver
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager


class Testing:

    def __init__(self):
        self.url = 'https://www.cowin.gov.in/'
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
        sleep(3)
        self.driver.maximize_window()
        self.driver.get(self.url)

    def findElementByLink(self, link):
        self.driver.find_element(By.LINK_TEXT, link).click()

    def Cowin(self):
        self.findElementByLink('FAQ')
        sleep(3)
        self.driver.switch_to.window(self.driver.window_handles[1])
        print('Title of first Tab:', self.driver.current_url)
        print('Window ID:', self.driver.current_window_handle)
        sleep(3)
        self.findElementByLink('PARTNERS')
        sleep(5)
        self.driver.switch_to.window(self.driver.window_handles[2])
        print('Title of second Tab:', self.driver.current_url)
        print('Window ID:', self.driver.current_window_handle)
        sleep(3)
        self.driver.close()


output = Testing()
output.Cowin()
output.driver.quit()

