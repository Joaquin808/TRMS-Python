from selenium.webdriver.chrome.webdriver import WebDriver


class EmployeeSubmittedFormPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def work_just(self):
        return self.driver.find_element_by_id("workJust")

    def submit_button(self):
        return self.driver.find_element_by_id("submitButton")
