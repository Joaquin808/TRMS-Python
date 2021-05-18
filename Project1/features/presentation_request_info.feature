Feature:

  Scenario: Project One Form Request Additional Information
    Given Employee is on the login page
    When The employee inputs the correct login credentials
    When The employee clicks the login button
    When The employee is on the employee information page
    When The employee clicks the submit new form page button
    When The employee is on the form submission page
    When The employee inputs all of the necessary information
    When The employee clicks the submission button
    Then The employee will be on the form submission page and return to employee information page

    When Supervisor is on the login page
    When The supervisor inputs their login credentials
    When The supervisor clicks the login button
    Then The supervisor is on their information page
    When The supervisor clicks view submitted reimbursement forms
    Then The supervisor will be able to view submitted reimbursement forms
    When The supervisor request additional information
    When The supervisor hits the submit button

    When The employee goes back to login
    When The employee inputs the correct login credentials
    When The employee clicks the login button
    When The employee is on the employee information page
    When The employee clicks view submitted reimbursement form
    When The employee is on the submitted form page
    When The employee inputs additional information
    Then The employee will be on the form submission page and return to employee information page


    When Supervisor is on the login page
    When The supervisor inputs their login credentials
    When The supervisor clicks the login button
    Then The supervisor is on their information page
    When The supervisor clicks view submitted reimbursement forms
    Then The supervisor will be able to view submitted reimbursement forms
    When The supervisor clicks approval checkbox
    When The supervisor hits the submit button
    Then The reimbursement form should be submitted and approval be viewable by employee

    When The dept head is on the login page
    When The dept head inputs their login credentials
    When The dept head clicks the login button
    Then The dept head is on the employee information page
    When The dept head clicks button to view submitted reimbursement forms
    Then The dept head will see submitted reimbursement forms
    When The dept head clicks dept head approval checkbox
    When The dept head clicks submit button
    Then The dept head will be on submission page and return to employee information page

    When The benco is on the login page
    When The benco inputs their login credentials
    When The benco clicks the login button
    Then The benco is on the employee information page
    When The benco clicks button to view submitted reimbursement forms
    Then The benco will see submitted reimbursement forms
    When The benco clicks benco approval checkbox
    When The benco clicks submit button
    Then The benco will be on submission page and return to employee information page

    When The dept head has rejected the form
    When The employee goes back to login
    When The employee refreshes the page
    Then The employee will see the updated values and know the form was rejected