import random


class EmployeeWage:

    def employeeattendance(self):
        attendance = random.randint(0, 1)
        if attendance == 0:
            print("Present")
        else:
            print("Absent")
        return attendance


if __name__ == '__main__':
    print("Welcome to Employee Wage Computation Program")
    employee = EmployeeWage()
    isPresent = employee.employeeattendance()
