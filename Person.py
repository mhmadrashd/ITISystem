class Person:
    moods = ("happy", "tired", "Lazy")

    def __init__(self, name, money, mood, healthRate):
        self.name = name
        self.__money = 0
        self.__healthRate = 0
        self.mood = mood

        self.money = money
        self.healthRate = healthRate

    def sleep(self, hours):
        if isinstance(hours, int):
            if hours < 7:
                self.mood = Person.moods[1]
            elif hours == 7:
                self.mood = Person.moods[0]
            elif hours > 7:
                self.mood = Person.moods[2]
            return self.mood
        else:
            print("***************************\nError Please Enter valid hours\n***************************")
            return 0

    def eat(self, meals):
        if isinstance(meals, int) and meals in (1, 2, 3):
            if meals == 1:
                self.__healthRate = "50%"
            elif meals == 2:
                self.__healthRate = "75%"
            elif meals == 3:
                self.__healthRate = "100%"
            return self.__healthRate
        else:
            print("***************************\nError Please Enter valid meals\n***************************")
            return 0

    def buy(self, items):
        if isinstance(items, int):
            if (items * 10) < self.__money:
                self.__money -= (10 * items)
            else:
                print("***************************\nCan't buy this items because you haven't money "
                      "enough\n***************************")
            return self.__money
        else:
            print("***************************\nError Please Enter valid items\n***************************")
            return 0

    @property
    def healthRate(self):
        return self.__healthRate

    @healthRate.setter
    def healthRate(self, health):
        if isinstance(health, int) and 0 <= health <= 100:
            self.__healthRate = health
        else:
            self.__healthRate = 80
            print("***************************\nError You Enter not valid health rate\nValue was set by default "
                  "value=80\n***************************")

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, val):
        if isinstance(val, int) and val >= 1000:
            self.__money = val
        else:
            self.__money = 1000
            print("***************************\nError You Enter not valid money\nValue was set by default "
                  "value=1000\n***************************")

# m = Person("mohamed", 100, "happy", 120)
# print(m.name)
# print(m.money)
# print(m.mood)


# print(m.buy(10))
# print(m.sleep(7))
# print(m.healthRate)
# print(m.eat(1))
# print(m.healthRate)
