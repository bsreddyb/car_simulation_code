import pytest
from src.car_simulation.simulation.field import Field
from src.car_simulation.simulation.car import Car
# Mock configuration (adjust based on actual config values)
class Config:
    CAR_DIRECTIONS = ['N', 'E', 'S', 'W']
    INVALID_COMMAND_MESSAGE = "Invalid command entered."
    INVALID_DIRECTION_MESSAGE = "Invalid direction entered."

# Test fixture for setting up field and car objects
@pytest.fixture
def field():
    return Field(10, 10)  # Create a 10x10 field for testing

@pytest.fixture
def car():
    return Car(name="Car1", x=5, y=5, direction='N', commands='FFLR')

# Test Car Initialization
def test_car_initialization():
    car = Car(name="CarTest", x=2, y=3, direction='E', commands='FFR')
    assert car.name == "CarTest"
    assert car.x == 2
    assert car.y == 3
    assert car.direction == 'E'
    assert car.commands == 'FFR'
    assert car.command_index == 0
    assert car.active is True

# Test car turn_left functionality
def test_turn_left(car):
    initial_direction = car.direction
    car.turn_left()
    assert car.direction == Config.CAR_DIRECTIONS[(Config.CAR_DIRECTIONS.index(initial_direction) - 1) % 4]

# Test car turn_right functionality
def test_turn_right(car):
    initial_direction = car.direction
    car.turn_right()
    assert car.direction == Config.CAR_DIRECTIONS[(Config.CAR_DIRECTIONS.index(initial_direction) + 1) % 4]

# Test move_forward functionality within bounds
def test_move_forward_within_bounds(car, field):
    car.move_forward(field)
    assert car.x == 5  # x shouldn't change
    assert car.y == 6  # y increases by 1 when facing North

# Test move_forward out of bounds
def test_move_forward_out_of_bounds():
    car = Car(name="CarTest", x=0, y=9, direction='N', commands='F')
    field = Field(10, 10)
    car.move_forward(field)
    assert car.x == 0
    assert car.y == 9  # No movement since it's out of bounds

# Test next_command functionality
def test_next_command(car):
    assert car.next_command() == 'F'  # First command should be 'F'
    car.execute_command(Field(10, 10))  # Execute the first command
    assert car.next_command() == 'F'  # Next command should also be 'F'

# Test command execution and car movement
def test_execute_command(car, field):
    car.execute_command(field)  # Execute first 'F'
    assert car.x == 5
    assert car.y == 6  # Car moved North

    car.execute_command(field)  # Execute second 'F'
    assert car.x == 5
    assert car.y == 7  # Car moved North again

    car.execute_command(field)  # Execute 'L' (turn left)
    assert car.direction == 'W'  # Car should now be facing West

    car.execute_command(field)  # Execute 'R' (turn right)
    assert car.direction == 'N'  # Car should be back facing North

# Test car inactivity due to invalid initialization
def test_invalid_car_name():
    with pytest.raises(ValueError):
        Car(name="", x=2, y=3, direction='E', commands='FFR')

def test_validate_car_name():
    car = Car(name="Car1", x=5, y=5, direction='N', commands='F')
    valid, message = Car.validate_car_name("Car2", [])
    assert valid is True
    assert message == "Valid car name."
    
    valid, message = Car.validate_car_name("", [])
    assert valid is False
    assert message == "Car name cannot be empty."
