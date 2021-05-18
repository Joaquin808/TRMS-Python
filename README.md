# **Tuition Reimbursement Management**

## **Project Description**
The Tuition Reimbursement System, TRMS, allows users to submit reimbursements for courses and training. 
The submitted reimbursement must be approved by that employee's supervisor, department head, and benefits coordinator. 
The benefits coordinator then reviews the grade received before finalizing the reimbursement.

### **Technologies Used**
- Python - version 3.9.4
- Selenium - verson 4
- Cucumber - version 7.2.1
- Flask - version 2.0.0
- psycopg2 2.8.6
- Flask-Cors 3.0.10
- PyCharm - version 2021.1.1
- JavaScript - version 1.8.5
- PostgreSQL - version 12
- HTML - version 5
- CSS - version 3
- Visual Studio Code - version 1.56
- DBeaver - version 21.0.5
- Postman - version 8.4.0

### **Features**
#### **List of features ready and TODOs for future development**

- The ability to login through various roles in the company, such as a regular employee, department supervisor,
department head and as a benefits coordinator
- A regular employee is capable of filling out a tuition reimbursement form and submit it for approval
- The various roles not including a regular employee, may view the tuition reimbursement form that has been submitted
and approve, deny or request additional information from the employee who has submitted the reimbursement form
- Once a form has been approved, denied, or additional information has been requested, the employee can 
view that form and will see at what stage the form has or has not been approved and resubmit the form, if applicable

#### **To-do-list**
- Allow management the ability to view all submitted forms or mutliple forms, then select which one they wish to view
at that moment rather than only displaying one form at a time

### **Getting Started**
1. Make sure you have Python 3 installed on your device
2. Clone my repository with this Git link and command in your command prompt, in your desired location:
 "git clone https://github.com/Joaquin808/TRMS-Python.git"
3. Set up the db_connection.py file with your AWS RDS database
4. Ensure that Flask, psycopg2, Flask-Cors is installed in the PyCharm terminal using the pip install commands
5. Run app.py and open up your web browser of choice via "Login.html" in the HTML folder 
