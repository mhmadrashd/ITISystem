from Person import *
from Car import *
import re

regexEmail = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


class Employee(Person):
    allEmp = []

    def __init__(self, name, mood, healthRate, email, salary, distanceToWork,
                 carName, carFuelRate, carVelocity):

        Person.__init__(self, name, salary, mood, healthRate)
        self.__empCar = Car(carName, carFuelRate, carVelocity)

        self.__email = None
        self.email = email

        self.__salary = None
        self.salary = salary

        self.distanceToWork = distanceToWork
        Employee.allEmp.append(self)

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, sal):
        if isinstance(sal, int) and sal >= 1000:
            self.__salary = sal
        else:
            self.__salary = 1000

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, eml):
        if re.fullmatch(regexEmail, eml):
            self.__email = eml
        else:
            print("***************************\nError Please Enter valid email\n***************************")

    @property
    def Car(self):
        return f"(Car Name: {self.__empCar.name}, Car Fuel Rate:" \
               f" {self.__empCar.fuelRate}, Car Velocity: {self.__empCar.velocity})"

    def work(self, hours):
        if isinstance(hours, int):
            if hours < 8:
                self.mood = Person.moods[2]
            elif hours == 8:
                self.mood = Person.moods[0]
            elif hours > 8:
                self.mood = Person.moods[1]
            return self.mood
        else:
            print("***************************\nError Please Enter valid hours\n***************************")
            return 0

    def drive(self, distance):
        return self.__empCar.run(self.__empCar.velocity, distance)

    def refuel(self):
        self.__empCar.fuelRate = 100

    def sendMail(self, to="default@gmail.com", subject="default subject mail", msg="default mail body",
                 receiver_name="default receiver name"):
        with open("mailFile.txt", "a") as mailFile:
            text = f'''\n-------------------- Email Header --------------------
            \nFrom: {self.email} To: {to}
            \nHi, {receiver_name}
            \n-------------------- Email Message --------------------
            \n {msg}
            \nthanks
            \n-------------------- Email Subject --------------------
            \n{subject}
************************************************************************************
            '''
            mailFile.write(text)


m = Employee("mohamed", "happy", 80, "mo@mo.mo", 8000, 30, "BMW", 100, 150)

# ######## Person Methods
# print(m.name)
# print(m.money)
# print(m.mood)
# print(m.buy(10))
# print(m.sleep(7))
# print(m.healthRate)
# print(m.eat(1))
# print(m.healthRate)

# ####### Employee Methods
# print(m.email)
# print(m.salary)
# print(m.Car)
# print(m.work(8))
# print(m.drive(20))
# print(m.drive(300))
# print(m.Car)
# m.refuel()
# print(m.Car)
# m.sendMail()
# print(Employee.allEmp[0].name)
# print(Employee.allEmp[0].money)
