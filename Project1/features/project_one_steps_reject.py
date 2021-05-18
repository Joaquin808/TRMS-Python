from time import sleep

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.employee_information_page import EmployeeInformationPage
from features.pages.fill_form_page import FillFormPage
from features.pages.form_approval_page import FormApprovalPage
from features.pages.form_submission_page import FormSubmissionPage
from features.pages.login_page import LoginPage
from services.form_service import FormService

driver: WebDriver = webdriver.Chrome(
    "G:/RevatureWork/SeleniumDrivers/chromedriver.exe")
login_page = LoginPage(driver)
employee_information_page = EmployeeInformationPage(driver)
fill_form_page = FillFormPage(driver)
form_submission_page = FormSubmissionPage(driver)
form_approval_page = FormApprovalPage(driver)


@given(u'Employee is on the login page')
def employee_get_to_login_page(context):
    driver.get("G:\RevatureWork\Project1\HTML\Login.html")


@when(u'The employee inputs the correct login credentials')
def employee_credentials(context):
    login_page.username().send_keys("jmbell")
    login_page.password().send_keys("password")


@when(u'The employee clicks the login button')
def employee_clicks_login(context):
    login_page.login_button().click()
    sleep(1)


@when(u'The employee is on the employee information page')
def employee_on_information_page(context):
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    assert "Employee Information" == driver.title
    sleep(1)


@when(u'The employee clicks the submit new form page button')
def employee_clicks_submit_new_form(context):
    employee_information_page.new_form_button().click()
    sleep(1)


@when(u'The employee is on the form submission page')
def employee_on_form_page(context):
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    assert driver.title == "Form"


@when(u'The employee inputs all of the necessary information')
def employee_fills_out_form(context):
    elements = fill_form_page.all_form_elements()
    elements[0].send_keys("Joaquin")
    elements[1].send_keys("Bell")
    elements[2].send_keys("2021-07-27")
    elements[3].send_keys("10:00")
    elements[4].send_keys("NC State")
    elements[5].send_keys("A C++ course")
    elements[6].send_keys("639.70")
    elements[7].send_keys("Exam")
    elements[8].send_keys("University Course")
    elements[9].send_keys("C")
    elements[10].send_keys("To increase my overall knowledge")
    sleep(1)


@when(u'The employee clicks the submission button')
def employee_submit_form(context):
    fill_form_page.submit_button().click()
    sleep(1)


@then(u'The employee will be on the form submission page and return to employee information page')
def step_impl(context):
    window_after = driver.window_handles[0]
    driver.switch_to.window(window_after)
    print(driver.title)
    assert driver.title == "Form Submission"
    form_submission_page.back_button().click()
    sleep(1)
    # driver.quit()
    # sleep(1)


@when(u'Supervisor is on the login page')
def supervisor_login_page(context):
    driver.get("G:\RevatureWork\Project1\HTML\Login.html")


@when(u'The supervisor inputs their login credentials')
def supervisor_input_credentials(context):
    login_page.username().send_keys("daf")
    login_page.password().send_keys("passw")


@when(u'The supervisor clicks the login button')
def super_login_button(context):
    login_page.login_button().click()
    sleep(1)


@then(u'The supervisor is on their information page')
def supervisor_on_information_page(context):
    assert driver.title == "Employee Information"


@when(u'The supervisor clicks view submitted reimbursement forms')
def supervisor_click_view_forms(context):
    employee_information_page.view_form_button().click()
    sleep(1)


@then(u'The supervisor will be able to view submitted reimbursement forms')
def supervisor_on_view_form_page(context):
    assert driver.title == "Department Supervisor"
    sleep(1)


@when(u'The supervisor clicks approval checkbox')
def supervisor_approve_form(context):
    form_approval_page.approval_button().click()
    sleep(1)


@when(u'The supervisor hits the submit button')
def supervisor_submit_approval(context):
    form_approval_page.submit_button().click()


@then(u'The reimbursement form should be submitted and approval be viewable by employee')
def step_impl(context):
    pass


@when(u'The dept head is on the login page')
def dept_head_login_page(context):
    driver.get("G:\RevatureWork\Project1\HTML\Login.html")


@when(u'The dept head inputs their login credentials')
def dept_head_login_credentials(context):
    login_page.username().send_keys("rsc")
    login_page.password().send_keys("pword")


@when(u'The dept head clicks the login button')
def dept_head_click_login(context):
    login_page.login_button().click()
    sleep(1)


@then(u'The dept head is on the employee information page')
def dept_head_information(context):
    assert driver.title == "Employee Information"


@when(u'The dept head clicks button to view submitted reimbursement forms')
def dept_head_view_form(context):
    employee_information_page.view_form_button().click()
    sleep(1)


@then(u'The dept head will see submitted reimbursement forms')
def dept_head_on_form_page(context):
    assert driver.title == "Department Supervisor"




