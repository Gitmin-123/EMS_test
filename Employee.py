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

    def add_employee(self, name, age, emp_id, department):
        #Exception for name must be string
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        
        #Exception for age must be int
        if not isinstance(age, int):
            raise TypeError("Age must be integers")
        
        #Exception for age must be int
        if not isinstance(emp_id, int):
            raise TypeError("ID must be integers")
        
        #Exception for age must be above 0 and below 60
        if age < 0 or age >= 60:
            raise ValueError("Age must be a non-negative integer below 60")
        
        #Exception for Id cannot be negative
        if emp_id < 0:
            raise ValueError("ID must be a non-negative integer")
        
        #Exception for department cannot be empty and should be within the category
        if not department:
            raise ValueError("Department cannot be empty")
        if department not in ["Engineering", "HR", "Marketing", "Finance", "IT"]:
            raise ValueError("Invalid department")

        employee = Employee(name, age, emp_id, department)
        self.employees.append(employee)

    def get_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                return employee
        raise ValueError("Employee not found with ID: {}".format(emp_id))

    def delete_employee_by_id(self, emp_id):
        for employee in self.employees:
            if employee.emp_id == emp_id:
                self.employees.remove(employee)
                return True
        return False



class TestEmployeeManagementSystem(unittest.TestCase):
    # Initialize the EmployeeManagementSystem and add initial employees
    def setUp(self):
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


    # Test adding, retrieving, and deleting an employee
    def test_delete_employee_by_id(self):
        self.assertFalse(self.system.delete_employee_by_id(999))  # Test deleting non-existent employee

    def test_add_get_delete_employee(self):
      # Add an employee
        self.system.add_employee("John Smith", 30, 3, "Engineering")

      # Retrieve the added employee
        employee = self.system.get_employee_by_id(3)  # Use ID 3
        self.assertIsNotNone(employee)
        self.assertEqual(employee.name, "John Smith")

    # Delete the employee
        self.assertTrue(self.system.delete_employee_by_id(3)) 

    # Verify the employee is deleted
        with self.assertRaises(ValueError):
         self.system.get_employee_by_id(3)  # Use ID 3

if __name__ == "__main__":
    unittest.main()