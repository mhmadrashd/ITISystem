import Emp
import ConnEmp


class Office:
    def __init__(self, name="ITI", employees=Emp.getEmpFromDB()):
        self.name = name
        self.employees = employees

    def get_all_employees(self):
        i = 0
        for emp in self.employees:
            i += 1
            print(f'''
            -----------(Employee Number:{i} in {self.name})--------------
            Name:{emp.name}\t\tEmail:{emp.email}
            Salary:{emp.salary}\t\tDistance:{emp.distanceToWork}
            Mode:{emp.mood}\t\tHealth Rate:{emp.healthRate}
            Car Name:{emp.Car[0]}\t\tCar Fuel Rate:{emp.Car[1]}
            Car Velocity:{emp.Car[2]}
            -----------------------------------------------------''')

    def get_employee(self, empId):
        emp = self.employees[empId]
        print(f'''
        -----------(Employee Number:{empId} in {self.name})--------------
        Name:{emp.name}\t\tEmail:{emp.email}
        Salary:{emp.salary}\t\tDistance:{emp.distanceToWork}
        Mode:{emp.mood}\t\tHealth Rate:{emp.healthRate}
        Car Name:{emp.Car[0]}\t\tCar Fuel Rate:{emp.Car[1]}
        Car Velocity:{emp.Car[2]}
        -----------------------------------------------------''')

    def hire(self, curEmp):
        if isinstance(curEmp, Emp.Employee):
            Emp.Employee(curEmp.name, curEmp.mood, curEmp.healthRate,
                         curEmp.email, curEmp.salary, curEmp.distanceToWork,
                         curEmp.Car[0], curEmp.Car[1], curEmp.Car[2])
            ConnEmp.insertNewEmp(curEmp.name, curEmp.mood, curEmp.healthRate,
                                 curEmp.email, curEmp.salary, curEmp.distanceToWork,
                                 curEmp.Car[0], curEmp.Car[1], curEmp.Car[2])
            print("Employee Hired Successfully")
        else:
            print("Error Enter Valid Employee Object")

    def fire(self, empId):
        empId = int(empId)
        if len(self.employees) >= empId:
            empId -= 1
            emp = self.employees[empId]
            self.employees.pop(empId)
            ConnEmp.DeleteEmpByEmailAndName(emp.name, emp.email)

    def calculate_lateness(self):
        pass

    def deduct(self):
        pass

    def reward(self):
        pass


# off = Office("ITI")
# off.get_all_employees()
# off.get_employee(2)

# m = Emp.Employee("Alaa", "happy", 50, "alaa@alaa.alaa", 20000, 10, "BMW", 100, 150)
# ConnEmp.insertNewEmp("Alaa", "happy", 50, "alaa@alaa.alaa", 20000, 10, "BMW", 100, 150)

# off.hire(m)

# off.get_all_employees()

# off.fire(3)
# off.get_all_employees()
