from selenium.webdriver.chrome.webdriver import WebDriver


class FormApprovalPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def approval_button(self):
        return self.driver.find_element_by_id("approval")

    def submit_button(self):
        return self.driver.find_element_by_id("submitButton")

    def reject_button(self):
        return self.driver.find_element_by_id("rejectForm")

    def deny_input(self):
        return self.driver.find_element_by_id("denyReason")

    def request_info(self):
        return self.driver.find_element_by_id("addInfo")
