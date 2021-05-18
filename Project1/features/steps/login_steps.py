from time import sleep

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.login_page import LoginPage

driver: WebDriver = webdriver.Chrome(
    "G:/RevatureWork/SeleniumDrivers/chromedriver.exe")


# @given('The employee is on the login page')
# def get_to_login_page(context):
#     driver.get('G:/RevatureWork/Project1/HTML/Login.html')
#
#
# @when('They input the correct login credentials')
# def input_credentials(context):
#     login_page = LoginPage(driver)
#     login_page.username().send_keys("jmbell")
#     login_page.password().send_keys("password")
#     sleep(1)
#
#
# @then('The employee should be on the form submission page')
# def click_login(context):
#     login_page = LoginPage(driver)
#     login_page.login_button().click()
#     driver.quit()
