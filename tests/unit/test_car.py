# tests/unit/test_car.py
import unittest
import pytest
from src.car_simulation.simulation.car import Car
from src.car_simulation.simulation.field import Field

class TestCar(unittest.TestCase):

    def setUp(self):
        # Set up a field and car object for testing
        self.field = Field(5, 5)
        self.car = Car("TestCar", 0, 0, 'N', "FFRFF")
    

    def test_initial_position_and_direction(self):
        # Test initial position and direction of the car
        self.assertEqual(self.car.x, 0)
        self.assertEqual(self.car.y, 0)
        self.assertEqual(self.car.direction, 'N')

    def test_set_commands_valid(self):
        # Test setting valid commands
        self.car.set_commands("FFLFFR")
        self.assertEqual(self.car.commands, "FFLFFR")

    def test_set_commands_invalid(self):
        # Test that setting invalid commands raises ValueError
        with pytest.raises(ValueError):
            self.car.set_commands("FFXFF")  # 'X' is invalid

    def test_move_forward_within_bounds(self):
        # Test moving forward within field bounds
        self.car.execute_command(self.field)  # F
        self.car.execute_command(self.field)  # F
        self.assertEqual((self.car.x, self.car.y), (0, 2))

    def test_turn_right_and_move_forward(self):
        # Set the initial position and direction explicitly for clarity
        self.car.x, self.car.y = 0, 0
        self.car.direction = 'N'
        
        # Step 1: Move forward twice
        self.car.set_commands("FF")
        self.car.execute_command(self.field)
        self.assertEqual((self.car.x, self.car.y), (0, 2))  # Expect (0, 2) after two forward moves
        
        # Step 2: Turn right
        self.car.set_commands("R")
        self.car.execute_command(self.field)
        self.assertEqual(self.car.direction, 'E')  # Expect direction to be 'E' after turning right
        
        # Step 3: Move forward twice in the new direction (East)
        self.car.set_commands("FF")
        self.car.execute_command(self.field)
        self.assertEqual((self.car.x, self.car.y), (2, 2))  # Expect (2, 2) after moving forward twice


    def test_turn_left_and_move_forward(self):
        # Test turning left and moving forward
        self.car.set_commands("LFF")  # Turn left (to 'W') and then move forward twice

        # Initial position (0,0), facing North
        self.car.execute_command(self.field)  # Execute "L", turn to West
        self.assertEqual(self.car.direction, 'W')  # Check direction after turn

        # Move forward once
        self.car.execute_command(self.field)  # Execute "F"
        # The car will try to move to (-1, 0), which is out of bounds, so it should stay at (0, 0)
        self.assertEqual((self.car.x, self.car.y), (0, 0))  # Position should not change

        # Move forward again
        self.car.execute_command(self.field)  # Execute "F"
        # Again, it will try to move out of bounds to (-1, 0)
        self.assertEqual((self.car.x, self.car.y), (0, 0))  # Position should still be (0, 0)

    def test_boundary_handling(self):
        # Test if car stops at the boundary
        self.car.set_commands("FFFFF")
        for _ in range(5):
            self.car.execute_command(self.field)
        self.assertTrue(self.field.within_bounds(self.car.x, self.car.y))

    def test_duplicate_name_validation(self):
        # Test for duplicate name validation
        existing_names = ["TestCar"]
        with pytest.raises(ValueError):
            valid, message = Car.validate_car_name("TestCar", existing_names)
            if not valid:
                raise ValueError(message)

    def test_representation(self):
        # Test car representation
        self.assertEqual(repr(self.car), "TestCar, (0,0) N, FFRFF")


if __name__ == '__main__':
    unittest.main()
