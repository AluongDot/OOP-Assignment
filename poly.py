class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement move()")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Test Polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()   # Each object responds differently to the same method
