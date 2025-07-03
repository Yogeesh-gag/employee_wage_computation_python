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

#UC3 Test: Call the function to display part-time wage
# Function to calculate the daily wage for a part-time employee
def calculate_part_time_wage():
    # Wage rate per hour (fixed)
    wage_per_hour = 20
    # Number of working hours for a part-time employee
    part_time_hour = 4
    # Calculate part-time daily wage
    daily_wage = wage_per_hour * part_time_hour
    print(f"Part Time Daily Wage: ${daily_wage}")

# UC4 Test: Using Match Statement
# Function to return employee working hours based on type using match-case
def get_employee_hours(emp_check):
    match emp_check:
        case 1:
            return 8 # Full-time
        case 2:
            return 4 # Part Time
        case _:
            return 0 # Absent

# Function to calculate daily wage using match-case logic
def calculate_wage_using_match():
    wage_per_hour=20
    # Randomly select 0=Absent, 1=Full-Time, 2=Part-Time
    emp_check=random.randint(0,2)
    emp_hours=get_employee_hours(emp_check)
    daily_wage=emp_hours*wage_per_hour

    # Print employee type and daily wage
    employee_types=['Absent','Full-Time','Part-Time']
    print(f"Employee Type: {employee_types[emp_check]}")
    print(f"Worked Hours: {emp_hours},Daily Wage: {daily_wage}")

#UC5 Test:
# Function to calculate employee wage for a full month
def calculate_monthly_wage():
    # wages rate per hour
    wage_per_hour = 20
    # Total number of working days in a month
    working_days = 20
    # Initialize total wage to 0
    total_wage = 0

    # loop through each working day
    for day in range(1, working_days + 1):
        # Randomly decide employee type (0 = Absent, 1 = Full-time, 2 = Part-time)
        emp_check = random.randint(0, 2)
        # Get hours worked based on wmployee type
        emp_hours = get_employee_hours(emp_check)
        # Calculate wage for the day
        daily_wage = emp_hours * wage_per_hour
        # Add daily wage to total wage
        total_wage += daily_wage

        # Print daily details
        print(f"Day {day}: Worked {emp_hours} hours, Daily Wage: {daily_wage}")

    # Print total wage after 20 days
    print(f"Total wage for {working_days} days: {total_wage}")