import math
import time


class Car:
    def __init__(self, name, fuel, vloc):
        self.validData = 0
        self.name = name
        self.__fuelRate = 0
        self.__velocity = 0
        self.fuelRate = fuel
        self.velocity = vloc
        self.__runState = 0
        self.__stopState = 0

    def run(self, velocity, distance):
        self.__runState = 1
        t = distance / velocity
        traveledDistance = 0  # 0km
        while self.__stopState == 0 and self.__fuelRate > 0 and distance > 0:
            distance -= 1  # -1km
            traveledDistance += 1  # +1km
            if traveledDistance % 10 == 0:
                self.__fuelRate -= self.__fuelRate * 0.1
                self.__fuelRate = math.floor(self.__fuelRate)
            state = ""
            if distance == 0:
                state = "Congratulations you have arrived"
            else:
                state = "Unfortunately you did not arrive"
        return f"Time= {t * 60}min, Remain Distance= {distance}km, Traveled Distance= {traveledDistance}km," \
               f" Fuel Rate = {self.__fuelRate}L\n{state}"

    def stop(self):
        if self.__runState == 1:
            self.__stopState = 1
        else:
            print("***************************\nThe car is already stopped\n***************************")

    @property
    def fuelRate(self):
        return self.__fuelRate

    @fuelRate.setter
    def fuelRate(self, fuel):
        if isinstance(fuel, int) and (0 <= fuel <= 100):
            self.__fuelRate = fuel
        else:
            self.__fuelRate = 70
            print("***************************\nError You Entered not valid fuel Rate\nData default = "
                  "70\n***************************")

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, vol):
        if isinstance(vol, int) and (0 <= vol <= 200):
            self.__velocity = vol
        else:
            self.__velocity = 120
            print("***************************\nError You Enter not valid velocity\nData default = "
                  "120\n***************************")


# m = Car("mohamed", 100, 100)
# print(m.name)
# print(m.fuelRate)
# print(m.velocity)

# print(m.run(100, 900))
#
# print(m.fuelRate)
