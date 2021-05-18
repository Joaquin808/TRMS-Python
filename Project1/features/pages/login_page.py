from selenium.webdriver.chrome.webdriver import WebDriver


class LoginPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def username(self):
        return self.driver.find_element_by_id('username')

    def password(self):
        return self.driver.find_element_by_id("password")

    def login_button(self):
        return self.driver.find_element_by_id("login")

