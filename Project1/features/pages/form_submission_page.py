from selenium.webdriver.chrome.webdriver import WebDriver


class FormSubmissionPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def back_button(self):
        return self.driver.find_element_by_id("homeButton")
