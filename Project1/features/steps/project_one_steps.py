from time import sleep

from behave import given, when, then
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver

from features.pages.employee_information_page import EmployeeInformationPage
from features.pages.employee_submitted_form_page import EmployeeSubmittedFormPage
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
employee_submitted_form_page = EmployeeSubmittedFormPage(driver)


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
    elements[2].send_keys("2021-04-30")
    elements[3].send_keys("08:00")
    elements[4].send_keys("Virginia")
    elements[5].send_keys("A test automation course")
    elements[6].send_keys("413.90")
    elements[7].send_keys("Exam")
    elements[8].send_keys("University Course")
    elements[9].send_keys("C")
    elements[10].send_keys("To get a greater a grasp of testing with automation")
    sleep(7)


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
    sleep(4)


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
    sleep(7)


@when(u'The supervisor hits the submit button')
def supervisor_submit_approval(context):
    form_approval_page.submit_button().click()
    sleep(1)


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
    sleep(3)


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
    sleep(10)


@when(u'The dept head clicks dept head approval checkbox')
def dept_head_click_approve(context):
    form_approval_page.approval_button().click()
    sleep(1)


@when(u'The dept head clicks submit button')
def dept_head_submit_approval(context):
    form_approval_page.submit_button().click()
    sleep(1)


@then(u'The dept head will be on submission page and return to employee information page')
def step_impl(context):
    pass


@when(u'The benco is on the login page')
def benco_on_login_page(context):
    driver.get("G:\RevatureWork\Project1\HTML\Login.html")


@when(u'The benco inputs their login credentials')
def benco_login_credentials(context):
    login_page.username().send_keys("akx")
    login_page.password().send_keys("wordp")


@when(u'The benco clicks the login button')
def benco_click_login(context):
    login_page.login_button().click()
    sleep(3)


@then(u'The benco is on the employee information page')
def benco_on_information_page(context):
    assert driver.title == "Employee Information"


@when(u'The benco clicks button to view submitted reimbursement forms')
def benco_clicks_view_form(context):
    employee_information_page.view_form_button().click()
    sleep(1)


@then(u'The benco will see submitted reimbursement forms')
def benco_views_submitted_form(context):
    assert driver.title == "Department Supervisor"
    sleep(3)


@when(u'The benco clicks benco approval checkbox')
def benco_approves_form(context):
    form_approval_page.approval_button().click()
    sleep(5)


@when(u'The benco clicks submit button')
def benco_submits_approval(context):
    form_approval_page.submit_button().click()
    sleep(1)


@then(u'The benco will be on submission page and return to employee information page')
def step_impl(context):
    pass


@when(u'All approvals have been checks and submitted')
def employee_login(context):
    driver.get("G:\RevatureWork\Project1\HTML\Login.html")


@when(u'The employee refreshes the page')
def employee_back_to_info_page(context):
    login_page.username().send_keys("jmbell")
    login_page.password().send_keys("password")
    login_page.login_button().click()
    sleep(3)


@then(u'The employee will see the updated values and will see reimbursement amount being given')
def employee_views_approved_form(context):
    employee_information_page.view_form_button().click()
    sleep(3)
    # driver.quit()
    FormService.delete_form(0)
    sleep(2)


@when(u'The dept head clicks dept head reject checkbox')
def dept_head_click_reject(context):
    form_approval_page.reject_button().click()


@when(u'The dept head provides a deny reason')
def dept_head_deny_reason(context):
    form_approval_page.deny_input().send_keys("The course isn't relevant to the job")
    sleep(3)


@when(u'The dept head has rejected the form')
def submit_rejection(context):
    # sleep(1)
    # form_approval_page.submit_button().click()
    sleep(1)


@when(u'The employee goes back to login')
def reopen_login_page(context):
    driver.get("G:\RevatureWork\Project1\HTML\Login.html")


@then(u'The employee will see the updated values and know the form was rejected')
def review_form(context):
    employee_information_page.view_form_button().click()
    sleep(4)
    # driver.quit()
    FormService.delete_form(0)
    sleep(1)


@when(u'The supervisor request additional information')
def sup_request_info(context):
    form_approval_page.request_info().click()


@when(u'The employee clicks view submitted reimbursement form')
def view_sub_reimb_forms(context):
    employee_information_page.view_form_button().click()


@when(u'The employee is on the submitted form page')
def step_impl(context):
    pass


@when(u'The employee inputs additional information')
def add_more_info(context):
    employee_submitted_form_page.work_just().send_keys(". This course is important because it will further improve "
                                                       "my understanding of OOP concepts.")
    sleep(5)
    employee_submitted_form_page.submit_button().click()
    sleep(1)

