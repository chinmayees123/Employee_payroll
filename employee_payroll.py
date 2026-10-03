import csv
from abc import ABC, abstractmethod
class Person(ABC):
    def __init__(self, name):
        self.__name = name
    def get_name(self):
        return self.__name
    def set_name(self, name):
        self.__name = name
    @abstractmethod
    def display(self):
        pass
class Employee(Person):
    def __init__(self, employee_id, name, basic_salary):
        super().__init__(name)
        self.__employee_id = employee_id
        self.__basic_salary = basic_salary
    def get_employee_id(self):
        return self.__employee_id
    def get_salary(self):
        return self.__basic_salary
    def calculate_salary(self):
        hra = self.__basic_salary * 0.10
        da = self.__basic_salary * 0.05
        return self.__basic_salary + hra + da
    def display(self):
        print("\nEmployee ID:", self.__employee_id)
        print("Name:", self.get_name())
        print("Basic Salary:", self.__basic_salary)
        print("Total Salary:", self.calculate_salary())
class FileManager:
    def save(self, employees):
        try:
            with open("payroll.csv", "w", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([
                    "Employee ID",
                    "Name",
                    "Basic Salary",
                    "Total Salary"
                ])
                for employee in employees:
                    writer.writerow([
                        employee.get_employee_id(),
                        employee.get_name(),
                        employee.get_salary(),
                        employee.calculate_salary()
                    ])
            print("Payroll data saved successfully.")
        except Exception:
            print("Error while saving file.")
employees = []
while True:
    print("\n===== EMPLOYEE PAYROLL SYSTEM =====")
    print("1. Add Employee")
    print("2. Calculate Salary")
    print("3. Generate Payslip")
    print("4. Search Employee")
    print("5. Save Payroll Data")
    print("6. Exit")
    choice = input("Enter choice: ")
    match choice:
        case "1":
            try:
                employee_id = input("Enter Employee ID: ")
                name = input("Enter Employee Name: ")
                salary = float(input("Enter Basic Salary: "))
                employee = Employee(
                    employee_id,
                    name,
                    salary
                )
                employees.append(employee)
                print("Employee added successfully.")
            except ValueError:
                print("Please enter a valid salary.")
        case "2":
            employee_id = input("Enter Employee ID: ")
            found = False
            for employee in employees:
                if employee.get_employee_id() == employee_id:
                    print("Total Salary:",
                          employee.calculate_salary())
                    found = True
                    break
            if not found:
                print("Employee not found.")
        case "3":
            employee_id = input("Enter Employee ID: ")
            found = False
            for employee in employees:
                if employee.get_employee_id() == employee_id:
                    print("\n===== PAYSLIP =====")
                    employee.display()
                    found = True
                    break
            if not found:
                print("Employee not found.")
        case "4":
            employee_id = input("Enter Employee ID: ")
            found = False
            for employee in employees:
                if employee.get_employee_id() == employee_id:
                    employee.display()
                    found = True
                    break
            if not found:
                print("Employee not found.")
        case "5":
            manager = FileManager()
            manager.save(employees)
        case "6":
            print("Thank you!")
            break
        case _:
            print("Invalid choice.")