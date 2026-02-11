class Passenger:
    def __init__ (self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def method(self):
        return self.name, self.age, self.sex
    def isAdult(self):
        if self.age>=18:
            return True
        else:
            return False
pass1 = Passenger("Николай", 15, "Мужской")
pass2 = Passenger("Багдан", 19, "Мужской")
print(pass1.method())
print(pass2.method())
print(pass1.isAdult(), pass2.isAdult())