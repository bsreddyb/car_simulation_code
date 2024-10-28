import unittest
import pytest
from src.car_simulation.simulation.car import Car
from src.car_simulation.simulation.field import Field


class TestCarIntegration(unittest.TestCase):

    def setUp(self):
        # Create a 5x5 field and initialize a car for tests
        self.field = Field(5, 5)
        self.car = Car("TestCar", 0, 0, 'N', "FFRFF")

    def test_initial_position_and_direction(self):
        # Check car's initial position and direction
        self.assertEqual(self.car.x, 0)
        self.assertEqual(self.car.y, 0)
        self.assertEqual(self.car.direction, 'N')

    def test_move_forward_within_bounds(self):
        # Execute forward commands and check position
        self.car.execute_command(self.field)  # F
        self.car.execute_command(self.field)  # F
        self.assertEqual((self.car.x, self.car.y), (0, 2))

    def test_turn_right_and_move_forward(self):
        # Execute commands to turn and move, check final position and direction
        self.car.execute_command(self.field)  # F
        self.car.execute_command(self.field)  # F
        self.car.execute_command(self.field)  # R
        self.car.execute_command(self.field)  # F
        self.car.execute_command(self.field)  # F
        self.assertEqual((self.car.x, self.car.y), (2, 2))
        self.assertEqual(self.car.direction, 'E')

    def test_turn_left_and_move_forward(self):
        # Check if turning left and moving forward updates position correctly
        car = Car("LeftTurnTestCar", 2, 2, 'N', "LFF")
        car.execute_command(self.field)  # L -> W
        car.execute_command(self.field)  # F
        car.execute_command(self.field)  # F
        self.assertEqual((car.x, car.y), (0, 2))
        self.assertEqual(car.direction, 'W')

    def test_boundary_handling(self):
        # Move car forward out of bounds and check if position stays within field
        boundary_car = Car("BoundaryTestCar", 0, 0, 'N', "FFFFF")
        for _ in range(5):
            boundary_car.execute_command(self.field)
        self.assertTrue(self.field.within_bounds(boundary_car.x, boundary_car.y))

    def test_duplicate_name_validation(self):
        # Attempt to create car with duplicate name, expect ValueError
        existing_names = ["TestCar"]
        with pytest.raises(ValueError):
            valid, message = Car.validate_car_name("TestCar", existing_names)
            if not valid:
                raise ValueError(message)

    def test_invalid_command(self):
        # Check if invalid commands raise a ValueError
        with pytest.raises(ValueError):
            Car("InvalidCommandCar", 0, 0, 'N', "FX")


    def test_representation(self):
        # Check car's representation string
        self.assertEqual(repr(self.car), "TestCar, (0,0) N, FFRFF")


if __name__ == '__main__':
    unittest.main()


