from selenium.webdriver.chrome.webdriver import WebDriver


class FillFormPage:

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def all_form_elements(self):
        elements = []
        elements.append(self.driver.find_element_by_id("fname"))
        elements.append(self.driver.find_element_by_id("lname"))
        elements.append(self.driver.find_element_by_id("eventDate"))
        elements.append(self.driver.find_element_by_id("eventTime"))
        elements.append(self.driver.find_element_by_id("location"))
        elements.append(self.driver.find_element_by_id("description"))
        elements.append(self.driver.find_element_by_id("cost"))
        elements.append(self.driver.find_element_by_id("gradingFormat"))
        elements.append(self.driver.find_element_by_id("typeOfEvent"))
        elements.append(self.driver.find_element_by_id("passingCutoff"))
        elements.append(self.driver.find_element_by_id("workJust"))
        return elements

    def submit_button(self):
        return self.driver.find_element_by_id("submitButton")
