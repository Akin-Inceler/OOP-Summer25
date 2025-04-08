# 1- Print "Hello World" on screen
print("Hello World")

# 2- Create a variable which show your age
age = 23

# 3- Display the type of variable in second question
print(type(age))

# 4- How many number types include in python and give examples
x = 1    # int
y = 2.8  # float
z = 1j   # complex

# 5- Create two list which is contain str and other one contain int. Finally gather two list in one list.
list1 = ["apple","banana"]
list2 = [1,2,3]
list3 = list1 + list2
print(list3)

# 6- Create a dictionary then update it.
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.update({"year": 2020})

# 7- Create a loop using list comprehension
thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]

# 8- Use math operators and multiply 8 by 6, add 4 and divide by 2.
x =(8*6+4)/2
print(x)

# 9- Create a while loop with break statement.
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# 10- Create a class which contains brands
class Brand:
  def __init__(self, name, type):
    self.name = name
    self.type = type

b1 = Brand("Nike", "Sport")
b2 = Brand("Volvo","Car")
b3 = Brand("Zara","Clothes")

print(b1.name)
print(b1.type)
print(b2.name)


