from selenium.webdriver.chrome.webdriver import WebDriver


class EmployeeInformationPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def new_form_button(self):
        return self.driver.find_element_by_id("newButton")

    def view_form_button(self):
        return self.driver.find_element_by_id("submittedButton")
