# Employee Payroll System

## 1. Project Title
Employee Payroll System

## 2. Project Description
The Employee Payroll System is a simple Python-based application used to manage employee payroll information.
The system allows the user to:
- Add employees
- Calculate salary
- Generate payslips
- Search employees
- Save payroll data
The project demonstrates important Object-Oriented Programming (OOP) concepts such as classes and objects, encapsulation, inheritance, abstraction, file handling, and exception handling.

## 3. Objectives
The main objectives of this project are:
1. To add and manage employee records.
2. To calculate employee salary.
3. To generate a simple payslip.
4. To search for an employee.
5. To save payroll information into a CSV file.
6. To demonstrate Python OOP concepts.
7. To handle invalid inputs and file errors.

## 4. Technologies Used
- Programming Language: Python
- IDE: Visual Studio Code
- File Format: CSV
- Python Modules:
  - csv
  - abc

## 5. Main Features
### 1. Add Employee
The user can add an employee by entering:
- Employee ID
- Employee Name
- Basic Salary

### 2. Calculate Salary
The system calculates the total salary using:
- Basic Salary
- HRA (10% of basic salary)
- DA (5% of basic salary)
Formula:
    Total Salary = Basic Salary + HRA + DA

### 3. Generate Payslip
The system displays a simple payslip containing:
- Employee ID
- Employee Name
- Basic Salary
- Total Salary

### 4. Search Employee
The user can search for an employee using the Employee ID.

### 5. Save Payroll Data
The payroll information can be saved into:
    payroll.csv

## 6. Classes Used
### Person
- Abstract base class.
- Stores the employee's name.
- Provides getter and setter methods.
- Contains the abstract `display()` method.

### Employee
- Inherits from `Person`.
- Stores employee ID and basic salary.
- Calculates the total salary.
- Displays employee information.

### FileManager
- Handles file operations.
- Saves payroll information into a CSV file.

## 7. OOP Concepts Demonstrated
### Classes and Objects
The project uses multiple classes and creates objects from the `Employee` class.
### Encapsulation
Private attributes are used to protect employee information.
Examples:
    __name
    __employee_id
    __basic_salary
Getter and setter methods are used to access or modify data.

### Inheritance
The `Employee` class inherits from the `Person` class.
    Person
       |
       ↓
    Employee

### Abstraction
`Person` is an abstract class created using the `abc` module.

### File Handling
Payroll information is saved in:
    payroll.csv

### Exception Handling
`try-except` is used to handle invalid salary input and file-related errors.

## 8. Menu Options
    ===== EMPLOYEE PAYROLL SYSTEM =====
    1. Add Employee
    2. Calculate Salary
    3. Generate Payslip
    4. Search Employee
    5. Save Payroll Data
    6. Exit

## 9. How to Run the Project
### Step 1
Open Visual Studio Code.

### Step 2
Create a folder named:
    Employee Payroll System

### Step 3
Create a Python file named:
    employee_payroll.py

### Step 4
Copy the Python source code into the file.

### Step 5
Open the VS Code terminal.

### Step 6
Run the program using:
    python employee_payroll.py

### Step 7
Select the required option from the menu.

## 10. Sample Data
Example employee:
    Employee ID: E101
    Employee Name: Chinmayee
    Basic Salary: 30000

Salary calculation:
    Basic Salary = 30000
    HRA = 3000
    DA = 1500
    Total Salary = 34500

## 11. Output File
After selecting Save Payroll Data, the program creates:
    payroll.csv

Example:
    Employee ID,Name,Basic Salary,Total Salary
    E101,Chinmayee,30000.0,34500.0

## 12. Error Handling
The program handles:
- Invalid salary input
- Invalid menu choices
- Searching for an employee who does not exist
- File saving errors

Example:
    Enter Basic Salary: abc
    Please enter a valid salary.

Another example:
    Enter Employee ID: E999
    Employee not found.

## 13. Project Files
    Employee Payroll System/
    |
    ├── employee_payroll.py
    ├── payroll.csv
    ├── README.md
    |
    └── screenshots/
        ├── add_employee.png
        ├── calculate_salary.png
        ├── generate_payslip.png
        ├── search_employee.png
        └── save_payroll.png

## 14. Conclusion
The Employee Payroll System is a simple Python application for managing employee payroll information. It provides features such as adding employees, calculating salary, generating payslips, searching employees, and saving payroll data.
The project demonstrates classes and objects, encapsulation, inheritance, abstraction, file handling, and exception handling.