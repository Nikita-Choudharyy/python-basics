# ----------------------------------
# Python OOP: Polymorphism
# ----------------------------------
# Polymorphism allows different classes
# to use the same method name with different behavior.

# -----------------------------
# Example 1: Method Overriding
# -----------------------------
class Animal:
    def sound(self):
        print("Animal makes a sound")

class Dog(Animal):
    def sound(self):
        print("Dog barks")

class Cat(Animal):
    def sound(self):
        print("Cat meows")

animals = [Dog(), Cat(), Animal()]

for animal in animals:
    animal.sound()

# -----------------------------
# Example 2: Polymorphism with Functions
# -----------------------------
def add(a, b, c=0):
    return a + b + c

print("Add 2 numbers:", add(5, 10))
print("Add 3 numbers:", add(5, 10, 15))

# -----------------------------
# Example 3: Duck Typing
# -----------------------------
class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def make_it_fly(obj):
    obj.fly()

bird = Bird()
plane = Airplane()

make_it_fly(bird)
make_it_fly(plane)

# -----------------------------
# Practice examples
# -----------------------------

# 1. Create Shape base class
class Shape:
    def area(self):
        print("Area calculation")

class Rectangle(Shape):
    def area(self):
        print("Area of rectangle")

class Circle(Shape):
    def area(self):
        print("Area of circle")

shapes = [Rectangle(), Circle()]

for shape in shapes:
    shape.area()
