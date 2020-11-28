import random


class EmployeeWage:
    wage_per_hour = 20
    hours_per_day = 0
    employee_daily_wage = 0
    FULL_TIME = 0
    PART_TIME = 1
    full_time_employee_hours = 8
    part_time_employee_hours = 4

    @classmethod
    def employee_attendance(cls):
        attendance = random.randint(0, 2)
        if attendance == EmployeeWage.FULL_TIME:
            print("Employee is present for : Full Time")
            EmployeeWage.hours_per_day = EmployeeWage.full_time_employee_hours
        elif attendance == EmployeeWage.PART_TIME:
            print("Employee is present for : Part time")
            EmployeeWage.hours_per_day = EmployeeWage.part_time_employee_hours
        else:
            print("Employee is Absent")
            EmployeeWage.hours_per_day = 0


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    employee_wage_for_a_month = 0
    for day in range(1, 21):
        print(f"day {day} : ")
        EmployeeWage.employee_attendance()
        EmployeeWage.employee_daily_wage = EmployeeWage.wage_per_hour * EmployeeWage.hours_per_day
        print(f"Employee's salary for day {day} is : {EmployeeWage.employee_daily_wage}")
        employee_wage_for_a_month = employee_wage_for_a_month + EmployeeWage.employee_daily_wage
    else:
        print(f"\nEmployee's Salary for the Entire Month is: {employee_wage_for_a_month}")
