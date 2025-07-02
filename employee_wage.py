import random

# Function to check whether the employee is present or absent
def check_employee_attendence():
    # Generate a random number: 0 for Absent, 1 for Present
    emp_check = random.randint(0, 1)

    # Check the result and print employee status
    if emp_check == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")
