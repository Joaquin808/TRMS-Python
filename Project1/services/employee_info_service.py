from daos.employee_info_dao import EmployeeInfoDAO


class EmployeeInfoService:
    employee_info_dao = EmployeeInfoDAO()

    @classmethod
    def get_employee_info_by_name(cls, employee_info):
        return cls.employee_info_dao.get_employee_info_by_name(employee_info)

    @classmethod
    def get_employee_info_by_id(cls, employee_id):
        return cls.employee_info_dao.get_employee_info_by_id(employee_id)
