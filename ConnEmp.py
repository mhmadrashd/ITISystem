def insertNewEmp(name, mood, healthRate, email, salary, distanceToWork,
                 empName, empFuelRate, empVelocity):
    name = str(name)
    mood = str(mood)
    healthRate = str(healthRate)
    email = str(email)
    salary = str(salary)
    distanceToWork = str(distanceToWork)
    empName = str(empName)
    empFuelRate = str(empFuelRate)
    empVelocity = str(empVelocity)
    try:  # if file exist
        # try to open file
        with open("employees.txt", "r") as dbFile:
            empList = dbFile.readlines()
            # Check if file is empty or not
            if len(empList) > 0:
                lastEmp = empList[len(empList) - 1]
                empId = int(lastEmp[0]) + 1
            else:
                empId = 1
    except:
        empId = 1
    # Convert emp info to list
    empList = [str(empId), name, mood, healthRate, email, salary, distanceToWork,
               empName, empFuelRate, empVelocity]
    empInfo = ":".join(empList)
    empInfo = empInfo.strip("\n")
    data = f"{empInfo}\n"
    try:
        with open("employees.txt", "a") as dbFile:
            dbFile.write(data)
    except:
        with open("employees.txt", "w") as dbFile:
            dbFile.write(data)
    print("#########################\nEmployee Data Inserted "
          "Successfully\n#########################\n")


def searchEmp(emp):
    emp = str(emp)
    try:
        with open("employees.txt", "r") as dbFile:
            allEmp = dbFile.readlines()
            resultEmp = []
            for currEmp in allEmp:
                currEmp = currEmp.strip("\n")
                empInfo = currEmp.split(":")
                if empInfo[1] == emp or empInfo[2] == emp or empInfo[3] == emp \
                        or empInfo[4] == emp or empInfo[5] == emp or empInfo[6] == emp\
                        or empInfo[7] == emp or empInfo[8] == emp or empInfo[9] == emp:
                    resultEmp.append(currEmp)
            return resultEmp
    except Exception as e:
        print(e)


def getEmpByID(emp):
    emp = str(emp)
    try:
        with open("employees.txt", "r") as dbFile:
            allEmp = dbFile.readlines()
            resultEmp = []
            for currEmp in allEmp:
                currEmp = currEmp.strip("\n")
                empInfo = currEmp.split(":")
                if empInfo[0] == emp:
                    resultEmp.append(currEmp)
            return resultEmp
    except Exception as e:
        print(e)


def viewAllEmp():
    try:
        with open("employees.txt", "r") as dbFile:
            allEmp = dbFile.readlines()
            resultEmp = []
            for currEmp in allEmp:
                currEmp = currEmp.strip("\n")
                resultEmp.append(currEmp)
            return resultEmp
    except Exception as e:
        print(e)


def viewAllEmpAsLists():
    try:
        with open("employees.txt", "r") as dbFile:
            allEmp = dbFile.readlines()
            resultEmp = []
            for currEmp in allEmp:
                currEmp = currEmp.strip("\n")
                empInfo = currEmp.split(":")
                resultEmp.append(empInfo)
            return resultEmp
    except Exception as e:
        print(e)


def DeleteEmpByID(emp):
    emp = str(emp)
    try:
        resultEmp = []
        with open("employees.txt", "r") as dbFile:
            allEmp = dbFile.readlines()
            for currEmp in allEmp:
                currEmp = currEmp.strip("\n")
                empInfo = currEmp.split(":")
                if empInfo[0] != emp:
                    resultEmp.append(currEmp)
                else:
                    print(f"---------------------\nemp {currEmp} Deleted\n---------------------")
        with open("employees.txt", "w") as dbwFile:
            for currRes in resultEmp:
                empInfo = currRes.strip("\n")
                data = f"{empInfo}\n"
                dbwFile.write(data)
    except Exception as e:
        print(e)


def DeleteEmpByEmailAndName(empName,empEmail):
    empName = str(empName)
    empEmail = str(empEmail)
    try:
        resultEmp = []
        with open("employees.txt", "r") as dbFile:
            allEmp = dbFile.readlines()
            for currEmp in allEmp:
                currEmp = currEmp.strip("\n")
                empInfo = currEmp.split(":")
                if empInfo[1] == empName and empInfo[4] == empEmail:
                    print(f"---------------------\nemp {currEmp} Deleted\n---------------------")
                else:
                    resultEmp.append(currEmp)

        with open("employees.txt", "w") as dbwFile:
            for currRes in resultEmp:
                empInfo = currRes.strip("\n")
                data = f"{empInfo}\n"
                dbwFile.write(data)
    except Exception as e:
        print(e)

# insertNewEmp("mohamed", "happy", 80, "mo@mo.mo", 8000, 30, "BMW", 100, 150)

# print(getEmpByID(1))

# print(searchEmp("mo@mo.mo"))

# print(viewAllEmp())

# DeleteEmpByID(2)

# print(viewAllEmpAsLists())

# DeleteEmpByEmailAndName("moh","mo@mo.mo")
