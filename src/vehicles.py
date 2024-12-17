class Vehicle(object):
    def __init__(self, model, make):
        self.model = model
        self.make = make


class Car(Vehicle):
    def __init__(self, model, make, max_speed):
        super().__init__(model, make)
        self.max_speed = max_speed


class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)
        self.capacity = capacity


def vehicle_factory(cls, *args, **kwargs):
    return cls(*args, **kwargs)
