# importing the employee_wage file to access the functions
import employee_wage
from employee_wage import EmployeeWage
from employee_wage import EmployeeWageUC8

if __name__ == '__main__':
    # UC1 Test: Call the function to test employee attendance
    employee_wage.check_employee_attendence()

    # UC2 Test: Call the function to calculate and print daily wage
    employee_wage.calculate_daily_wage()

    # UC3 Test: Call the function to display part-time wage
    employee_wage.calculate_part_time_wage()

    # UC4 Test Using match-case
    employee_wage.calculate_wage_using_match()

    # UC5 Test call the function to compute monthly wage
    employee_wage.calculate_monthly_wage()

    # UC6 Test: Call the function to compute wage with working hour/day constraints
    employee_wage.calculate_wage_till_condition()

    # UC7 Test: Call class method to compute wage
    EmployeeWage.compute_employee_wage()

    # UC8 Test:  Example usage for multiple companies with different wage/hour/day constraints
    EmployeeWageUC8.compute_employee_wage("TCS", 25, 20, 100)
    EmployeeWageUC8.compute_employee_wage("Infosys", 20, 22, 120)
    EmployeeWageUC8.compute_employee_wage("Wipro", 18, 26, 110)
