class Passenger:
    def __init__ (self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex
    def method(self):
        return self.name, self.age, self.sex
    def is_adult(self):
        if self.age>=18:
            return True
        else: 
            return False
    def is_minor(self):
        if self.age>=40:
            return True
        else:
            return False
    @classmethod 
    def make_passenger(cls):
        name_input = input("Введите имя пассажира: ")
        age_input = int(input("Введите возраст пассажира: "))
        sex_input = input("Введите пол пассажира м/ж: ")
        return cls(name_input, age_input, sex_input)
        
        
pass1 = Passenger("Николай", 15, "Мужской")
pass2 = Passenger("Багдан", 19, "Мужской")
pass3 = Passenger.make_passenger()
print(pass1.method())
print(pass2.method())
print(pass3.method())
print(pass1.is_adult(), pass2.is_minor(), pass3.is_minor())