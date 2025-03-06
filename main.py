class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. My address is {self.address}"
p1 = Person("Akin Inceler" , 23, "Zaczek Dormitory")
print(p1.greet())