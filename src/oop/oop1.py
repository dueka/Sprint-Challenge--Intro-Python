# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class


class Vehicle:  # This is the base class
    def __init__(self, name, model, engine, description=""):
        self.name = name
        self.model = model
        self.engine = engine
        self.description = description

    def __str__(self):
        return f"The manufacturer of this vehicle is {self.name} and the model is {self.model} and the engine type is {self.engine}"


class GroundVehicle(Vehicle):
    def __init__(self, name, model, engine, category, description=""):
        super().__init__(name, model, engine, category, description=description)
        self.category = category


class Car(GroundVehicle):
    def __init__(self, name, model, engine, CarClass, description=""):
        super().__init__(name, model, engine, description=description)
        self.CarClass = CarClass


class Motorcycle(GroundVehicle):
    def __init__(self, name, model, engine, MotorcycleClass, description=""):
        super().__init__(self, name, model, engine, description="")
        self.MotorcycleClass = MotorcycleClass


class FlightVehicle(Vehicle):
    def __init__(self, name, model, engine, description=""):
        super().__init__(self, name, model, engine, description=description)


class Airplane(FlightVehicle):
    def __init__(self, name, model, engine, no_of_engine, description=""):
        super().__init__(self, name, model, engine, description=description)
        self.no_of_engine = no_of_engine


class Starship(FlightVehicle):
    def __init__(self, name, model, engine, no_of_engine, type_of_fuel, description=""):
        super().__init__(self, name, model, engine, description=description)
        self.type_of_fuel = type_of_fuel
