import unittest

from exceptions.employee_info_exception import EmployeeInfoException
from exceptions.login_exception import LoginException
from models.form import Form
from unit_tests.form_test import FormTest
from unit_tests.login_test import LoginTest


class TestMain(unittest.TestCase):

    def test_login_success(self):
        login = LoginTest.test_login(username="jmbell", password="password")
        self.assertEqual(login["id"], 0)

    def test_login_failure(self):
        try:
            login = LoginTest.test_login(username="jmbell", password="word")
            self.assertIsNone(login)
        except LoginException as le:
            print(le.message)

    def test_form_success(self):
        json = {"fname": "Joaquin", "lname": "Bell", "eventDate": "2021-04-17", "eventTime": "08:00",
                "location": "Virginia", "description": "A University Course", "cost": 8932.01,
                "typeOfEvent": "university course", "workJust": "To better myself"}
        form = FormTest.submitting_form_test(Form.json_parse(json))
        self.assertEqual(form["employeeId"], 0)

    def test_form_failure_no_employee(self):
        try:
            json = {"fname": "Joaquin", "lname": "Daniel", "eventDate": "2021-04-17", "eventTime": "08:00",
                    "location": "Virginia", "description": "A University Course", "cost": 8932.01,
                    "typeOfEvent": "university course", "workJust": "To better myself"}
            form = FormTest.submitting_form_test(Form.json_parse(json))
            self.assertIsNone(form)
        except EmployeeInfoException as e:
            print(e)

    def test_form_success_id_matches_employee(self):
        json = {"fname": "Mia", "lname": "Coronado", "eventDate": "2021-04-17", "eventTime": "08:00",
                "location": "Virginia", "description": "A University Course", "cost": 8932.01,
                "typeOfEvent": "university course", "workJust": "To better myself"}
        form = FormTest.submitting_form_test(Form.json_parse(json))
        self.assertNotEqual(form["employeeId"], 0)


if __name__ == '__main__':
    unittest.main()
