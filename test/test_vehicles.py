import unittest
from src.vehicles import Vehicle, Truck, Car, vehicle_factory


class TestVehicles(unittest.TestCase):

    def test_car(self):
        car = Car(make="Toyota", model="Auris", max_speed=200)
        self.assertIsInstance(car, Car)
        self.assertIsInstance(car, Vehicle)

    def test_track(self):
        truck = Truck(make="Scania", model="IX-200", capacity=20000)
        self.assertIsInstance(truck, Truck)
        self.assertIsInstance(truck, Vehicle)
        self.assertNotIsInstance(truck, Car)

    def test_factory(self):
        vehicle = vehicle_factory(Car, model="Jimny", make="Suzuki", max_speed=160)
        self.assertIsInstance(vehicle, Car)


if __name__ == "__main__":
    unittest.main()
