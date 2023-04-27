
class Vehicle:
    def __init__(self, name,color):

        self.name = name
        self.color = color
        print(self.name)
        print(color)

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"


class Bus(Vehicle):

    def seating_capacity(self, capacity=50):
        return super().seating_capacity(capacity=50)


School_bus = Bus("School Volvo","red")

print(School_bus.seating_capacity())