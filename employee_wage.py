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
    wage_per_hour = 20  # Fixed wage per hour (in currency units)
    full_day_hour = 8  # Fixed number of working hours in a full day
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
            return 8  # Full-time
        case 2:
            return 4  # Part Time
        case _:
            return 0  # Absent


# Function to calculate daily wage using match-case logic
def calculate_wage_using_match():
    wage_per_hour = 20
    # Randomly select 0=Absent, 1=Full-Time, 2=Part-Time
    emp_check = random.randint(0, 2)
    emp_hours = get_employee_hours(emp_check)
    daily_wage = emp_hours * wage_per_hour

    # Print employee type and daily wage
    employee_types = ['Absent', 'Full-Time', 'Part-Time']
    print(f"Employee Type: {employee_types[emp_check]}")
    print(f"Worked Hours: {emp_hours},Daily Wage: {daily_wage}")


#UC5 Test: Employee Wage for a full month
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


# UC6 Test: Calculate employee wage until condition
# Function to calculate employee wage until either max working hours or max working days is reached
def calculate_wage_till_condition():
    wage_per_hour = 20  # Fixed wage per hour
    max_hours = 100  # Maximum allowed working hours in a month
    max_days = 20  # Maximum allowed working days in a month

    total_hours = 0  # Accumulator for total hours worked
    total_days = 0  # Accumulator for total days worked
    total_wage = 0  # Accumulator for total wage

    # Loop continues until either total_hours reaches 100 or total_days reaches 20
    while total_hours < max_hours and total_days < max_days:
        total_days += 1  # Increment working day
        emp_check = random.randint(0, 2)  # Randomly decide employee type: 0 = Absent, 1 = Full-time, 2 = Part-time
        emp_hours = get_employee_hours(emp_check)  # Get working hours for the day based on employee type
        total_hours += emp_hours  # Add daily hours to total hours
        daily_wage = emp_hours * wage_per_hour  # Calculate wage for the day
        total_wage += daily_wage  # Add daily wage to total wage

        # Print daily status
        print(f"Day {total_days}: Worked {emp_hours} hrs, Daily Wage: ₹{daily_wage}")

    # Final output after loop ends
    print(f"\nTotal Days Worked: {total_days}")
    print(f"Total Hours Worked: {total_hours}")
    print(f"Total Wage: {total_wage}")


# UC7 Refactor using class, class variables and class method
class EmployeeWage:
    wage_per_hour = 20  # Fixed wage rate per hour
    full_day_hour = 8  # Working hours for full-time employee
    part_time_hour = 4  # Working hours for part-time employee
    max_hours_in_month = 100  # Maximum total working hours allowed in a month
    max_working_days = 20  # Maximum working days allowed in a month

    # Class method to compute employee wage
    @classmethod
    def compute_employee_wage(cls):
        total_hours = 0  # To store total hours worked
        total_days = 0  # To count total working days
        total_wage = 0  # To accumulate total wage

        # Loop until maximum hours or maximum working days are reached
        while total_hours < cls.max_hours_in_month and total_days < cls.max_working_days:
            total_days += 1
            # Randomly decide employee status: 0 = Absent, 1 = Full-time, 2 = Part-time
            emp_check = random.randint(0, 2)

            # Determine working hours based on attendance
            if emp_check == 1:
                emp_hours = cls.full_day_hour  # Full-Time
            elif emp_check == 2:
                emp_hours = cls.part_time_hour  # Part-time
            else:
                emp_hours = 0  # Absent

            total_hours += emp_hours  # Add daily hours to total
            daily_wage = emp_hours * cls.wage_per_hour  # Calculate daily wage
            total_wage += daily_wage  # Accumulate total wage

            # Print daily report
            print(f"Day {total_days}: Hours = {emp_hours}, Daily Wage = ₹{daily_wage}")

        # Final total wage output
        print(f"\nTotal Wage for the Employee: {total_wage}")

# UC8: Compute employee wage for multiple companies using a static method
class EmployeeWageUC8:

    # Static method since we are passing all required data as parameters (no need to access class state)
    @staticmethod
    def compute_employee_wage(company, wage_per_hour, max_days, max_hours):
        total_hours = 0     # Accumulator for total hours worked
        total_days = 0      # Counter for total days worked
        total_wage = 0      # Accumulator for total wage earned

        print(f"\nComputing wages for company: {company}")  # Display company name

        # Loop until either total working hours or days reach their respective limits
        while total_hours < max_hours and total_days < max_days:
            total_days += 1
            emp_check = random.randint(0, 2)  # 0 = Absent, 1 = Full-time, 2 = Part-time

            # Assign working hours based on employee status
            if emp_check == 1:
                emp_hours = 8  # Full-time
            elif emp_check == 2:
                emp_hours = 4  # Part-time
            else:
                emp_hours = 0  # Absent

            total_hours += emp_hours                  # Update total working hours
            daily_wage = emp_hours * wage_per_hour    # Calculate wage for the day
            total_wage += daily_wage                  # Add to total wage

            # Print day-wise summary
            print(f"Day {total_days}: Hours = {emp_hours}, Daily Wage = {daily_wage}")

        # Final output after all days or hours are used
        print(f"Total wage for {company}: {total_wage}")
