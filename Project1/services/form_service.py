from daos.form_dao import FormDAO
from models.employee_info import EmployeeInfo
from services.employee_info_service import EmployeeInfoService


class FormService:
    form_dao = FormDAO()
    employee_info_service = EmployeeInfoService()

    @classmethod
    def get_all_forms_for_employee(cls, employee_id):
        return cls.form_dao.get_all_forms_for_employee(employee_id)

    @classmethod
    def submit_form(cls, form):
        # Get employee information to check to see if they exist
        employee_info = EmployeeInfo()
        employee_info.fname = form.fname
        employee_info.lname = form.lname
        returned_employee = cls.employee_info_service.get_employee_info_by_name(employee_info)
        # -------------------------------------------
        returned_form = cls.form_dao.submit_form(form)
        returned_form["employeeId"] = returned_employee["id"]
        return returned_form

    @classmethod
    def approve_form(cls, form, employee_id):
        # Update the form, so the employee can see whether or not it has been approved or
        # the supervisor is requesting additional information
        # Get employee information to check to see if they exist
        employee_info = EmployeeInfo()
        employee_info.fname = form.fname
        employee_info.lname = form.lname
        returned_employee = cls.employee_info_service.get_employee_info_by_name(employee_info)

        updated_form = cls.form_dao.update_form(form, employee_id)
        updated_form["employeeId"] = returned_employee["id"]
        return updated_form

    @classmethod
    def request_info(cls, form, employee_id):
        pass

    @classmethod
    def delete_form(cls, employee_id):
        cls.form_dao.delete_form(employee_id)
