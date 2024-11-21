#ASSG 1
# Base Class: Car
class Car:
    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.brand} {self.model} is driving!")

    def stop(self):
        print(f"The {self.brand} {self.model} has stopped.")

# Subclass: ElectricCar
class ElectricCar(Car):
    def __init__(self, brand, model, color, battery_capacity):
        super().__init__(brand, model, color)
        self.battery_capacity = battery_capacity

    def charge(self):
        print(f"The {self.brand} {self.model} is charging with a {self.battery_capacity} kWh battery.")

    def drive(self):  # Overriding the drive method
        print(f"The silent {self.color} electric {self.brand} {self.model} is driving smoothly!")

# Create objects
tesla = ElectricCar("Tesla", "Model S", "Red", 100)
toyota = Car("Toyota", "Corolla", "Blue")

# Test methods
tesla.drive()
tesla.charge()
tesla.stop()

print("\n---\n")

toyota.drive()
toyota.stop()



#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#ASSG 2


# Base Class: Vehicle
class Vehicle:
    def move(self):
        print("The vehicle is moving.")

# Subclass: Car
class Car(Vehicle):
    def move(self):
        print("The car is driving 🚗.")

# Subclass: Plane
class Plane(Vehicle):
    def move(self):
        print("The plane is flying ✈️.")

# Subclass: Boat
class Boat(Vehicle):
    def move(self):
        print("The boat is sailing 🚤.")

# Subclass: Bicycle
class Bicycle(Vehicle):
    def move(self):
        print("The bicycle is pedaling 🚴.")

# Test Polymorphism
vehicles = [Car(), Plane(), Boat(), Bicycle()]

for vehicle in vehicles:
    vehicle.move()















