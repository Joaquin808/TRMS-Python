from time import sleep

from behave import given, when, then

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.fill_form_page import FillFormPage

driver: WebDriver = webdriver.Chrome(
    "G:/RevatureWork/SeleniumDrivers/chromedriver.exe")


# @given(u'Employee is on the form webpage')
# def get_form_page(context):
#     driver.get('G:/RevatureWork/Project1/HTML/EmployeeForm.html')
#
#
# @when(u'Employee inputs valid information')
# def fill_out_form(context):
#     elements = FillFormPage(driver).all_form_elements()
#     elements[0].send_keys("Joaquin")
#     elements[1].send_keys("Bell")
#     elements[2].send_keys("2021-04-30")
#     elements[3].send_keys("08:00")
#     elements[4].send_keys("virginia")
#     elements[5].send_keys("A test automation course")
#     elements[6].send_keys("1350.90")
#     elements[7].send_keys("Exam")
#     elements[8].send_keys("University Course")
#     elements[9].send_keys("A")
#     elements[10].send_keys("To increase my overall knowledge")
#
#
# @when(u'Employee hits the submit button')
# def submit_form(context):
#     form_page = FillFormPage(driver)
#     form_page.submit_button().click()
#     sleep(1)
#
#
# @then(u'The form is submitted to their direct supervisor')
# def after_submission(context):
#     driver.quit()
