class EmployeeSystem:
    def __init__(self):
        self.__employees = []

    def addEmployees(self, name, position, salary):
        employee = {
            "name":name,
            "position":position,
            "salary":salary
        }
        int(employee["salary"])
        self.__employees.append(employee)
        print(name, "has been added to the employee list")

    def displayEmployees(self):
        if len(self.__employees) == 0:
            print("No employees found")
        else:
            print("\nEMPLOYEES:")
            print("================")
            for employee in self.__employees:
                print("Name:", employee["name"])
                print("Position:", employee["position"])
                print("Salary: $",employee["salary"])
                print("-------------------------------------------")
    
    def searchEmployee(self, name):
        for employee in self.__employees:
            if employee["name"].lower() == name.lower():
                print("Employee Located")
                print("Name: ", employee["name"])
                print("Position: ", employee["position"])
                print("Salary: $",employee["salary"])
                print("-------------------------------------------")
                return
            print("Employee not found")

    def increaseSalary(self, name, amount):
        for employee in self.__employees:
            if employee["name"].lower() == name.lower():
                employee["salary"] += amount

employees = EmployeeSystem()

num_of_additions = int(input("How many employees do you want to input (integer): "))
for i in range(num_of_additions):
    print("\nEnter Employees:", i + 1)

    name = input("Enter employee name: ")
    position = input("Enter employee position: ")
    salary = int(input("Enter employee salary: $"))

    employees.addEmployees(name, position, salary)

employees.displayEmployees()

searchEmployee = input("\nEnter employee name: ")
employees.searchEmployee(searchEmployee)

adjust = input("Enter 'yes' to adjust an employees salary: ").lower()
if adjust == "yes":
    name = input("Enter employee name:")
    amount = int(input("Enter amount to add to salary (integer): $"))
    employees.increaseSalary(name, amount)
    employees.displayEmployees()
else:
    print("No salaries adjusted")