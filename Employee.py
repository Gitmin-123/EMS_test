import unittest

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


class TestEmployeeManagementSystem(unittest.TestCase):
    def setUp(self):
        # Initialize the EmployeeManagementSystem and add initial employees
        self.system = EmployeeManagementSystem()
        self.system.add_employee("Hasan Mubarak", 30, 1, "HR")
        self.system.add_employee("Jon Smith", 25, 2, "IT")

    # Test adding a new employee
    def test_add_employee(self):
        self.assertEqual(len(self.system.employees), 2)
        self.system.add_employee("Marker burg", 28, 3, "Marketing")
        self.assertEqual(len(self.system.employees), 3)

    # Test retrieving an employee by ID
    def test_get_employee_by_id(self):
        employee = self.system.get_employee_by_id(1)
        self.assertIsNotNone(employee)
        self.assertEqual(employee.name, "Hasan Mubarak")

    # Test deleting an employee by ID
    def test_delete_employee_by_id(self):
        self.assertTrue(self.system.delete_employee_by_id(2))
        self.assertEqual(len(self.system.employees), 1)
        self.assertFalse(self.system.delete_employee_by_id(999))

    # Test adding an employee with an invalid name
    def test_add_employee_invalid_name(self):
        with self.assertRaises(TypeError):
            self.system.add_employee(123, 30, 4, "Finance")
        self.assertEqual(len(self.system.employees), 2)



if __name__ == "__main__":
    ems = EmployeeManagementSystem()
    ems.add_employee('Ekram', 22, 1, 'IT')
    employee = ems.get_employee_by_id(1)
    print("Employee Name:", employee.name, ' department:',employee.department, ' age:',employee.age, ' emp_id:',employee.emp_id)
