# tests/integration/test_car_integration.py
import unittest
import pytest
from src.car_simulation.simulation.car import Car
from src.car_simulation.simulation.field import Field

class TestCarIntegration(unittest.TestCase):

    def setUp(self):
        # Initialize a 5x5 field and a car for tests
        self.field = Field(5, 5)
        self.car = Car("TestCar", 0, 0, 'N', "FFRFF")

    def test_initial_position_and_direction(self):
        self.assertEqual(self.car.x, 0)
        self.assertEqual(self.car.y, 0)
        self.assertEqual(self.car.direction, 'N')

    def test_move_forward_within_bounds(self):
        self.car.execute_command(self.field)
        self.car.execute_command(self.field)
        self.assertEqual((self.car.x, self.car.y), (0, 2))

    def test_turn_right_and_move_forward(self):
        self.car.execute_command(self.field)
        self.car.execute_command(self.field)
        self.car.execute_command(self.field)
        self.car.execute_command(self.field)
        self.car.execute_command(self.field)
        self.assertEqual((self.car.x, self.car.y), (2, 2))
        self.assertEqual(self.car.direction, 'E')

    def test_turn_left_and_move_forward(self):
        car = Car("LeftTurnTestCar", 2, 2, 'N', "LFF")
        car.execute_command(self.field)
        car.execute_command(self.field)
        car.execute_command(self.field)
        self.assertEqual((car.x, car.y), (0, 2))
        self.assertEqual(car.direction, 'W')

    def test_turn_left_and_move_forward(self):
        car = Car("LeftTurnTestCar", 2, 2, 'N', "LFF")
        print(f"Initial position: ({car.x}, {car.y}), direction: {car.direction}")
        car.execute_command(self.field)  # Turn left
        print(f"After turning left: ({car.x}, {car.y}), direction: {car.direction}")
        car.execute_command(self.field)  # Move forward
        print(f"After first move forward: ({car.x}, {car.y}), direction: {car.direction}")
        car.execute_command(self.field)  # Move forward again
        print(f"Final position: ({car.x}, {car.y}), direction: {car.direction}")
        self.assertEqual((car.x, car.y), (0, 2))


    def test_boundary_handling(self):
        boundary_car = Car("BoundaryTestCar", 0, 0, 'N', "FFFFF")
        for _ in range(5):
            boundary_car.execute_command(self.field)
        self.assertTrue(self.field.within_bounds(boundary_car.x, boundary_car.y))

    def test_duplicate_name_validation(self):
        existing_names = ["TestCar"]
        with pytest.raises(ValueError):
            valid, message = Car.validate_car_name("TestCar", existing_names)
            if not valid:
                raise ValueError(message)

    def test_invalid_command(self):
        with pytest.raises(ValueError):
            self.car.set_commands("FX")  # Invalid command 'X' should raise ValueError

    def test_representation(self):
        self.assertEqual(repr(self.car), "TestCar, (0,0) N, FFRFF")

if __name__ == '__main__':
    unittest.main()
