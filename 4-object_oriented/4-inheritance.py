class Animal:
    def eat(self):
        print("Animal-EAT")
# ------------------------------------------------------

# Animal -- Parent or Base Class
# Mammal,Fish : Child or Derived Class

# class Child(Parent)



# ------------------------------------------------------

class Mammal(Animal):
    def walk(self):
        print("Mammal- Walk")

class Fish(Animal):
    def swim(self):
        print("Fish- Swim")

# ------------------------------------------------------

m=Mammal()
m.eat()
m.walk()

print("--------------------------------")

f=Fish()
f.eat()
f.swim()