from exceptions.employee_info_exception import EmployeeInfoException
from models.employee_info import EmployeeInfo
from util.db_connection import connection


class EmployeeInfoDAO:

    @staticmethod
    def get_employee_info_by_name(employee_info):
        sql = "SELECT * FROM employee_info WHERE fname = %s AND lname = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (employee_info.fname, employee_info.lname))
        connection.commit()
        info = cursor.fetchone()
        if info:
            return EmployeeInfo(info[0], info[1], info[2], info[3]).json()
        else:
            raise EmployeeInfoException(
                f"Employee with name {employee_info.fname} {employee_info.lname} doesn't exist")

    @staticmethod
    def get_employee_info_by_id(employee_id):
        sql = "SELECT * FROM employee_info WHERE id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
        info = cursor.fetchone()
        if info:
            return EmployeeInfo(info[0], info[1], info[2], info[3]).json()
        else:
            print("Employee doesn't exist")

