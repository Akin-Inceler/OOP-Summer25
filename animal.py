class Animal:
    def __init__(self, name, group, number_of_legs, skills):
        self.name = name
        self.group = group
        self.number_of_legs = number_of_legs
        self.skills = skills

animals = [
    Animal(name="Cat", group="Mammals", number_of_legs=4, skills=["climbing", "jumping"]),
    Animal(name="Dog", group="Mammals", number_of_legs=4, skills=["running", "fetching"]),
    Animal(name="Eagle", group="Birds", number_of_legs=2, skills=["flying", "hunting"]),
    Animal(name="Shark", group="Fish", number_of_legs=0, skills=["swimming", "hunting"]),
    Animal(name="Frog", group="Amphibians", number_of_legs=4, skills=["jumping", "swimming"]),
]


for animal in animals:
    print(f"Name: {animal.name}")
    print(f"Group: {animal.group}")
    print(f"Number of Legs: {animal.number_of_legs}")
    print(f"Skills: {', '.join(animal.skills)}\n")
