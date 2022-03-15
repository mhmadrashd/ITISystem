import Emp


def main():
    print("1-Create Employee\n2-List All Employees\n3-Search Employee\n4-Exit")
    msg1 = input("Enter Number of your choice: ")

    while not msg1.isdigit():
        msg1 = input("Please Enter Valid Data\nEnter Number of your choice: ")
    msg1 = int(msg1)
    match msg1:
        case 1:  # Insert Employee Page
            return Emp.insertEmp()
        case 2:  # All Employee Page
            return Emp.listAllEmp()
        case 3:  # Search Employee Page
            return Emp.searchEmp()
        case 4:  # Exit
            exit()
        case _:
            print("----------------------------")
            print("Enter Valid Number")
            print("----------------------------")
            return main()
