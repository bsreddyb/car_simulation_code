# simulation/car.py
#from simulation.field import Field  # Using absolute import
from .field import Field  
from car_simulation.config.config import Config
from localize.localize import localizations
from utils.logger import Logger

class Car:
    """
        Car Class
        Attributes:
            name : str -> The name of the car.
            x : int    -> The x-coordinate of the car's position.
            y : int    -> The y-coordinate of the car's position.
            direction : str -> The direction the car is facing ('N', 'E', 'S', 'W').
    
            commands : list  -> The list of commands for the car to execute.
    """
    
    DIRECTIONS = Config.CAR_DIRECTIONS

    def __init__(self, name: str, x: int, y: int, direction: str, commands: str):
        """
        A Constructer to initilize all the necessary attributes for the car object.
        """

        self.name: str = name
        self.x: int = x
        self.y: int = y
        self.direction: str = direction
        self.commands: str = commands
        self.command_index: int = 0
        self.active: bool = True  # Set to False if the car stops (collision, etc.)
        self.logger = Logger.setup_logger('CAR')

        # Validate the car name during initialization
        try:
            existing_names = []  # You can replace this with actual list of existing names
            valid, message = self.validate_car_name(name, existing_names)
            if not valid:
                raise ValueError(message)
        except ValueError as e:
            print(f"Error initializing car: {e}")
            self.active = False  # Mark car as inactive if name is invalid

    @staticmethod
    def validate_car_name(name: str, existing_names: list) -> tuple:
        """Validate if the car name is valid: non-null, non-empty, 
        alphanumeric, and not a duplicate.
        """
        try:
            if name is None:
                return False, "Car name cannot be None."
            elif len(name) == 0:
                return False, "Car name cannot be empty."
            elif not name.isalnum():
                return False, "Car name must only contain alphanumeric characters."
            elif name in existing_names:
                return False, "Car name must be unique; it already exists."
            else:
                return True, "Valid car name."
        except Exception as e:
            return False, f"An error occurred during validation: {e}"

    def turn_left(self) -> None:
        """Turn the car left."""
        try:
            current_index = Car.DIRECTIONS.index(self.direction)
            self.direction = Car.DIRECTIONS[(current_index - 1) % 4]
        except ValueError as e:
            print(f"Error turning left: {e}")

    def turn_right(self) -> None:
        """Turn the car right."""
        try:
            current_index = Car.DIRECTIONS.index(self.direction)
            self.direction = Car.DIRECTIONS[(current_index + 1) % 4]
        except ValueError as e:
            print(f"Error turning right: {e}")

    def move_forward(self, field: Field) -> None:
        """Move forward by one unit in the current direction if within bounds."""
        try:
            if self.direction == 'N':
                new_x, new_y = self.x, self.y + 1
            elif self.direction == 'E':
                new_x, new_y = self.x + 1, self.y
            elif self.direction == 'S':
                new_x, new_y = self.x, self.y - 1
            elif self.direction == 'W':
                new_x, new_y = self.x - 1, self.y
            
            if field.within_bounds(new_x, new_y):
                self.x, self.y = new_x, new_y  # Update position only if within bounds
            else:
                print("Move out of bounds; position not updated.")
        except Exception as e:
            print(f"Error moving forward: {e}")

    def next_command(self) -> str:
        """Return the next command to execute, or None if commands are exhausted."""
        try:
            if self.command_index < len(self.commands):
                return self.commands[self.command_index]
            return None
        except Exception as e:
            print(f"Error fetching next command: {e}")
            return None

    def execute_command(self, field: Field) -> None:
        """Execute the next command for the car."""
        if not self.active:
            print(f"{self.name} is inactive and cannot execute commands.")
            return
        command = self.next_command()
        try:
            if command == 'L':
                self.turn_left()
            elif command == 'R':
                self.turn_right()
            elif command == 'F':
                self.move_forward(field)
            self.command_index += 1
        except Exception as e:
            print(f"Error executing command '{command}': {e}")

    def __repr__(self) -> str:
        return f"{self.name}, ({self.x},{self.y}) {self.direction}, {self.commands}"
