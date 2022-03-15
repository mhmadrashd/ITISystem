import re
import Office
import Emp

regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def checkValidMail(email):
    if re.fullmatch(regexEmail, email):
        return False
    else:
        return True


def enterEmployeeData():
    print("****************************************************")
    moods = ("happy", "tired", "Lazy")

    empName = input("Enter Employee Name: ")
    while len(empName) == 0 or (not empName.isalpha()):
        empName = input("You Must Enter Valid Name\nEnter Employee Name: ")

    mood = input(f"Enter Employee Mood From {moods}: ")
    while len(mood) == 0 or (not mood.isalpha()) or not (mood in moods):
        mood = input(f"You Must Enter Valid Mood\nEnter Employee Mood From {moods}: ")

    healthRate = input("Enter Employee Health Rate: ")
    while not healthRate.isdigit():
        healthRate = input("Please Enter Valid Health Rate\nEnter Employee Health Rate: ")
    healthRate = int(healthRate)

    email = input("Enter Your Email: ")
    while checkValidMail(email):
        email = input("You Must Enter Valid Email\nEnter Your Email: ")

    salary = input("Enter Employee Salary: ")
    while not salary.isdigit():
        salary = input("Please Enter Valid Salary\nEnter Employee Salary: ")
    salary = int(salary)

    distance = input("Enter Employee Distance To Work(KM): ")
    while not distance.isdigit():
        distance = input("Please Enter Valid Distance\nEnter Employee Distance To Work: ")
    distance = int(distance)

    carName = input("Enter Employee Car Name: ")
    while len(carName) == 0 or (not carName.isalpha()):
        carName = input("You Must Enter Valid Car Name\nEnter Employee Car Name: ")

    carFuelRate = input("Enter Employee Car Fuel Rate: ")
    while not carFuelRate.isdigit():
        carFuelRate = input("Please Enter Valid Car Fuel Rate\nEnter Employee Car Fuel Rate: ")
    carFuelRate = int(carFuelRate)

    carVelocity = input("Enter Employee Car Velocity: ")
    while not carVelocity.isdigit():
        carVelocity = input("Please Enter Valid Car Velocity\nEnter Employee Car Velocity: ")
    carVelocity = int(carVelocity)

    empData = [empName, mood, healthRate, email, salary, distance, carName, carFuelRate, carVelocity]
    return empData


def SearchEmployee():
    print("****************************************************")
    empID = input("Enter Employee ID: ")
    while not empID.isdigit():
        empID = input("Please Enter Valid Employee ID\nEnter Employee ID: ")
    empID = int(empID)
    return empID


def ManageEmployee():
    while True:
        print("****************************************************")
        print("1-Hire Employee\n2-Fire Employee\n3-Back")
        msg1 = input("Enter Number of your choice: ")
        while not msg1.isdigit():
            msg1 = input("Please Enter Valid Data\nEnter Number of your choice: ")
        msg1 = int(msg1)
        match msg1:
            case 1:  # Hire Employee Page
                empData = enterEmployeeData()
                empObj = Emp.Employee(empData[0], empData[1], empData[2], empData[3], empData[4], empData[5],
                                      empData[6], empData[7], empData[8])
                off = Office.Office()
                off.hire(empObj)
            case 2:  # Fire Employee
                off = Office.Office()
                off.fire(SearchEmployee())
            case 3:  # Back
                return
            case _:
                print("----------------------------")
                print("Enter Valid Number")
                print("----------------------------")
