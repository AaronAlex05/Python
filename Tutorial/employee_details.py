class Employee:
    """Base class for all employees."""
    def __init__(self, name, id, salary):
        self.name = name
        self.id = id
        self.salary = salary

    def display(self):
        """Displays base employee details."""
        print(f"ID: {self.id}")
        print(f"Name: {self.name}")
        print(f"Salary: ${self.salary:,}")

class Manager(Employee):
    """Subclass representing a Manager, demonstrating use of super()."""
    def __init__(self, name, id, salary, department):
        super().__init__(name, id, salary)
        self.department = department

    def display(self):
        """Displays manager details, including those from the base class."""
        print("--- Employee Details ---")
        super().display()
        print(f"Department: {self.department}")
        print("-------------------------")

def main():
    # Instantiate a Manager object
    mgr = Manager("Alice Johnson", "MGR-001", 95000, "Human Resources")
    
    # Display the details
    mgr.display()

if __name__ == "__main__":
    main()
