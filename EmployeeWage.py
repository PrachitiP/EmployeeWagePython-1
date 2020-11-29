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
        presence = random.randint(0, 2)
        return presence

    @classmethod
    def employee_work_hours(cls, attendance_of_employee):
        switch = {
            0: EmployeeWage.full_time_employee_hours,
            1: EmployeeWage.part_time_employee_hours,
            2: 0
        }
        EmployeeWage.hours_per_day = switch.get(attendance_of_employee)
        print(EmployeeWage.hours_per_day)


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    EmployeeWage.employee_work_hours(EmployeeWage.employee_attendance())
    EmployeeWage.employee_daily_wage = EmployeeWage.wage_per_hour * EmployeeWage.hours_per_day
    print(f"Employee's Salary for the day is {EmployeeWage.employee_daily_wage}")
