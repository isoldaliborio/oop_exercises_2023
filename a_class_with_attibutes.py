#  Source: https://pynative.com/python-object-oriented-programming-oop-exercise/
# 1 Create a Class with instance attributes

# Write a Python program to create a Vehicle class
# with max_speed and mileage instance attributes.


class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage


modelX = Vehicle("volvo", 240, 18)
print(modelX.max_speed, modelX.mileage)



# 3. Create a child class Bus that will inherit all the variables and methods of the Vehicle class

class Bus(Vehicle):
    def seating_capacity(self, capacity):
        self.capacity = 50



school_bus = Bus("Volvo", 180, 12)
print(f"Vehicle Name {school_bus.name} Speed: {school_bus.max_speed}, Mileage: {school_bus.mileage}")


# 4 Class inheritance
# Create a Bus class that inherits from the Vehicle class.
# Give the capacity argument of Bus.seating_capacity() a default value of 50.


