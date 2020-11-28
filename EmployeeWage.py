import random


class EmployeeWage:
    wage_per_hour = 20
    hours_per_day = 0
    employee_daily_wage = 0

    @classmethod
    def employee_attendance(cls):
        attendance = random.randint(0, 1)
        if attendance == 0:
            print("Present")
            EmployeeWage.hours_per_day = 8
        else:
            print("Absent"), cls


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    EmployeeWage.employee_attendance()
    EmployeeWage.employee_daily_wage = EmployeeWage.wage_per_hour*EmployeeWage.hours_per_day
    print(f"Employee's Salary for the day is {EmployeeWage.employee_daily_wage}")
