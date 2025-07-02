import random

#UC1 To Check Employee Attendance
# Function to check whether the employee is present or absent
def check_employee_attendence():
    # Generate a random number: 0 for Absent, 1 for Present
    emp_check = random.randint(0, 1)

    # Check the result and print employee status
    if emp_check == 1:
        print("Employee is Present")
    else:
        print("Employee is Absent")

# UC2-calculate and print daily wage
# Function to calculate daily wage of an employee
def calculate_daily_wage():
    wage_per_hour = 20      # Fixed wage per hour (in currency units)
    full_day_hour = 8       # Fixed number of working hours in a full day
    daily_wage = wage_per_hour * full_day_hour  # Calculate daily wage
    print(f"Daily Wage: ${daily_wage}")  # Display the calculated daily wage


# Function to calculate the daily wage for a part-time employee
def calculate_part_time_wage():
    # Wage rate per hour (fixed)
    wage_per_hour = 20
    # Number of working hours for a part-time employee
    part_time_hour = 4
    # Calculate part-time daily wage
    daily_wage = wage_per_hour * part_time_hour
    print(f"Part Time Daily Wage: ${daily_wage}")