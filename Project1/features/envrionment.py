from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.fill_form_page import FillFormPage
from features.pages.login_page import LoginPage

# ALl setup and teardown functions must go in this file
# These functions must be named using behave's conventions


def before_all(context):
    driver: WebDriver = webdriver.Chrome(
        "G:/RevatureWork/SeleniumDrivers/chromedriver.exe")
    context.driver = driver
    context.login_page = LoginPage(driver)
    context.fill_form_page = FillFormPage(driver)
    print("started")


def after_all(context):
    context.driver.quit()
    print("ended")
