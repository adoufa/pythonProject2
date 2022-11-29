class Human:

    def __init__(self, age = 0):
        self.set_age(age)
    @property
    def age(self):
        return self.__age()

    @age.setter
    def age(self, age):
        if 0 < age > 120:
            self.__age = age
        else:
            self.__age = 0


h = Human(age=90)
print(h.age())