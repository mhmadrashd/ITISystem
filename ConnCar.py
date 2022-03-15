def insertNewCar(name, fuelRate, velocity):
    name = str(name)
    fuelRate = str(fuelRate)
    velocity = str(velocity)
    try:  # if file exist
        # try to open file
        with open("cars.txt", "r") as dbFile:
            carList = dbFile.readlines()
            # Check if file is empty or not
            if len(carList) > 0:
                lastCar = carList[len(carList) - 1]
                carId = int(lastCar[0]) + 1
            else:
                carId = 1
    except:
        carId = 1
    # Convert car info to list
    carList = [str(carId), name, fuelRate, velocity]
    carInfo = ":".join(carList)
    carInfo = carInfo.strip("\n")
    data = f"{carInfo}\n"
    try:
        with open("cars.txt", "a") as dbFile:
            dbFile.write(data)
    except:
        with open("cars.txt", "w") as dbFile:
            dbFile.write(data)
    print("#########################\nCar Data Inserted "
          "Successfully\n#########################\n")


def searchCar(car):
    car = str(car)
    try:
        with open("cars.txt", "r") as dbFile:
            allCars = dbFile.readlines()
            resultCar = []
            for currCar in allCars:
                currCar = currCar.strip("\n")
                carInfo = currCar.split(":")
                if carInfo[1] == car or carInfo[2] == car or carInfo[3] == car:
                    resultCar.append(currCar)
            return resultCar
    except Exception as e:
        print(e)


def getCarByID(car):
    car = str(car)
    try:
        with open("cars.txt", "r") as dbFile:
            allCars = dbFile.readlines()
            resultCar = []
            for currCar in allCars:
                currCar = currCar.strip("\n")
                carInfo = currCar.split(":")
                if carInfo[0] == car:
                    resultCar.append(currCar)
            return resultCar
    except Exception as e:
        print(e)


def viewAllCars():
    try:
        with open("cars.txt", "r") as dbFile:
            allCars = dbFile.readlines()
            resultCars = []
            for currCars in allCars:
                currCars = currCars.strip("\n")
                resultCars.append(currCars)
            return resultCars
    except Exception as e:
        print(e)


def DeleteCarByID(car):
    car = str(car)
    try:
        resultCar = []
        with open("cars.txt", "r") as dbFile:
            allCars = dbFile.readlines()
            for currCar in allCars:
                currCar = currCar.strip("\n")
                CarInfo = currCar.split(":")
                if CarInfo[0] != car:
                    resultCar.append(currCar)
                else:
                    print(f"---------------------\nCar {currCar} Deleted\n---------------------")
        with open("cars.txt", "w") as dbwFile:
            for currRes in resultCar:
                CarInfo = currRes.strip("\n")
                data = f"{CarInfo}\n"
                dbwFile.write(data)
    except Exception as e:
        print(e)


# insertNewCar("BMW", "100", "200")

# print(getCarByID(7))

# print(searchCar(200))

# print(viewAllCars())

# DeleteCarByID(2)

# print(viewAllCars())
