# importing the employee_wage file to access the functions
import employee_wage

if __name__ == '__main__':
    # UC1 Test: Call the function to test employee attendance
    employee_wage.check_employee_attendence()

    # UC2 Test: Call the function to calculate and print daily wage
    employee_wage.calculate_daily_wage()

    # UC3 Test: Call the function to display part-time wage
    employee_wage.calculate_part_time_wage()

    # UC4 Test Using match-case
    employee_wage.calculate_wage_using_match()
