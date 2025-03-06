class Person:
    def __init__(self, name, age, index, nationality):
        self.name = name
        self.age = age
        self.index = index
        self.nationality = nationality

    def greet(self):
        return f"Hello, my name is {self.name} and I am {self.age} years old. My index number {self.index} and nationality {self.nationality}"
p1 = Person("Akin Inceler" , 23, 25525, "Turkey")
p2= Person("Ahmet Solmaz", 20, 25654, "Turkey")
p3=Person("John Dom", 21, 25956, "USA")
print(p1.greet())
print(p2.greet())
print(p3.greet())