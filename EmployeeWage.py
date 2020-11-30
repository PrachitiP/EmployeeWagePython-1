import random


class EmployeeWage:
    wage_per_hour = 20
    hours_per_day = 0
    employee_daily_wage = 0
    FULL_TIME = 0
    PART_TIME = 1
    full_time_employee_hours = 8
    part_time_employee_hours = 4
    monthly_wage_data = {}
    employee_wage_for_a_month = 0

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

    @classmethod
    def calculate_wage(cls,):
        emp_hours = 0
        day = 1
        while (emp_hours < 100) and (day < 20):
            daily_wage_data = {}
            print(f"day {day} : ")
            attendance = EmployeeWage.employee_attendance()
            EmployeeWage.employee_work_hours(attendance)
            emp_hours = emp_hours + EmployeeWage.hours_per_day
            if emp_hours > 100:
                diff = emp_hours - 100
                EmployeeWage.hours_per_day -= diff
                emp_hours -= diff
            EmployeeWage.employee_daily_wage = EmployeeWage.wage_per_hour * EmployeeWage.hours_per_day
            print(f"Employee's salary for day {day} is : {EmployeeWage.employee_daily_wage}")
            EmployeeWage.employee_wage_for_a_month += EmployeeWage.employee_daily_wage
            daily_wage_data[f"{EmployeeWage.employee_daily_wage}"] = f"{EmployeeWage.employee_wage_for_a_month}"
            EmployeeWage.monthly_wage_data[day] = daily_wage_data
            day = day + 1
        print(f"Employee hours : {emp_hours} and Days : {day}")


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    EmployeeWage.calculate_wage()
    print(f"\nEmployee's Salary for the Entire Month is: {EmployeeWage.employee_wage_for_a_month}")
    print(f"\n{EmployeeWage.monthly_wage_data}")
