from daos.employee_info_dao import EmployeeInfoDAO
from models.form import Form
from util.db_connection import connection


class FormDAO:

    @staticmethod
    def get_all_forms_for_employee(employee_id):
        sql = "SELECT * FROM form WHERE employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
        form = cursor.fetchone()
        if form:
            new_form = Form(form[0], form[1], form[2], form[3], form[4], form[5], form[6], form[7], form[8], form[9],
                            form[10], form[11], form[12], form[13], form[14], form[15], form[16], form[17],
                            form[18], form[19]).json()

            return new_form

    @staticmethod
    def submit_form(form):
        sql = "INSERT INTO form VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, " \
              "%s) RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (
            form.fname, form.lname, form.event_date, form.event_time, form.location, form.description, form.cost,
            form.grading_format, form.type_of_event, form.employee_id, form.passing_cutoff, form.urgent,
            form.final_grade, form.work_just, form.add_info, form.reject_form, form.deny_reason, form.dsup_approval,
            form.dhead_approval,
            form.benco_approval))
        connection.commit()
        record = cursor.fetchone()
        if record:
            return Form(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                        record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15],
                        record[16], record[17], record[18], record[19]).json()
        else:
            print("Failed to retrieve form record")

    @staticmethod
    def update_form(form, employee_id):
        employee_info_dao = EmployeeInfoDAO
        employee = employee_info_dao.get_employee_info_by_id(employee_id)

        approval_type = ""
        approval_answer = False
        if "department supervisor" in employee["erole"]:
            approval_type = "dsup_approval"
            approval_answer = form.dsup_approval
        elif "department head" in employee["erole"]:
            approval_type = "dhead_approval"
            approval_answer = form.dhead_approval
        elif "benco" in employee["erole"]:
            approval_type = "benco_approval"
            approval_answer = form.benco_approval

        # If a form was rejected, we need to only worry about updating that rather than who approved it
        if form.reject_form:
            approval_type = "reject_form"
            approval_answer = form.reject_form

        sql = f"UPDATE form SET {approval_type} = %s, deny_reason = %s, work_just = %s WHERE employee_id = %s " \
              f"RETURNING *"
        cursor = connection.cursor()
        cursor.execute(sql, (approval_answer, form.deny_reason, form.work_just, 0))
        connection.commit()
        record = cursor.fetchone()
        if record:
            return Form(record[0], record[1], record[2], record[3], record[4], record[5], record[6], record[7],
                        record[8], record[9], record[10], record[11], record[12], record[13], record[14], record[15],
                        record[16], record[17], record[18], record[19]).json()
        else:
            print("Failed to retrieve form record")

    @staticmethod
    def delete_form(employee_id):
        sql = "DELETE FROM form WHERE employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        connection.commit()
