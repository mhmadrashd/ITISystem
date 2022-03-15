import Emp
import SystemIn
import ConnEmp
import Office


def main():
    while True:
        print("****************************************************")
        print("1-Create Employee\n2-List All Employees\n3-Search Employee\n4-Manage Employee\n5-Exit")
        msg1 = input("Enter Number of your choice: ")

        while not msg1.isdigit():
            msg1 = input("Please Enter Valid Data\nEnter Number of your choice: ")
        msg1 = int(msg1)
        match msg1:
            case 1:  # Insert Employee Page
                empData = SystemIn.enterEmployeeData()
                empObj = Emp.Employee(empData[0], empData[1], empData[2], empData[3], empData[4], empData[5],
                                      empData[6], empData[7], empData[8])
                ConnEmp.insertNewEmp(empObj.name, empObj.mood, empObj.healthRate, empObj.email,
                                     empObj.salary, empObj.distanceToWork,
                                     empObj.Car[0], empObj.Car[1], empObj.Car[2])
            case 2:  # All Employee
                off = Office.Office()
                off.get_all_employees()
            case 3:  # Search Employee Page
                empData = SystemIn.SearchEmployee()
                off = Office.Office()
                off.get_employee(empData - 1)
            case 4:  # Manage Employee Page
                SystemIn.ManageEmployee()
            case 5:  # Exit
                exit()
            case _:
                print("----------------------------")
                print("Enter Valid Number")
                print("----------------------------")


main()
