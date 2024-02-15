class Employee:
    def __init__(self, name, age, emp_id, department):
        self.name = name
        self.age = age
        self.emp_id = emp_id
        self.department = department

class EmployeeManagementSystem:
    def __init__(self):
        self.employees = []

    
    # Adding employee       
    def add_employee(self, name, age, emp_id, department):
        employee = Employee(name, age, emp_id, department)
        self.employees.append(employee)

    # Retreiveing employee by id
    def get_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
        raise False

    # delete by employee id
    def delete_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return True
        return False

if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    ems.add_employee('Ekram', 22, 1, 'IT')
    employee = ems.get_employee_by_id(1)
    print("Employee Name:", employee.name, ' department:',employee.department, ' age:',employee.age, ' emp_id:',employee.emp_id)
