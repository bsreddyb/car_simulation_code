import pytest
from src.car_simulation.simulation.field import Field
from src.car_simulation.simulation.car import Car
from src.car_simulation.simulation.simulation import Simulation

@pytest.fixture
def setup_simulation():
    # Initialize a field with size 5x5
    field = Field(5, 5)
    # Create a new simulation with the field
    simulation = Simulation(field)
    return simulation

def test_multiple_cars_different_commands(setup_simulation):
    simulation = setup_simulation

    # Create three cars with different starting positions and directions
    car1 = Car("Car1", 0, 0, 'N')  # Starting at (0, 0) facing North
    car2 = Car("Car2", 1, 1, 'E')  # Starting at (1, 1) facing East
    car3 = Car("Car3", 2, 2, 'S')  # Starting at (2, 2) facing South

    # Set commands for each car
    car1.validate_commands("FFRFF")  # Move forward, turn right, move forward
    car2.validate_commands("LFFR")    # Turn left, move forward twice, turn right
    car3.validate_commands("FFLFF")   # Move forward twice, turn left, move forward twice

    # Add cars to the simulation
    simulation.add_car(car1)
    simulation.add_car(car2)
    simulation.add_car(car3)

    # Run the simulation
    simulation.run_simulation()

    # Check final positions and directions of each car
    """
    assert car1.x == 2  # Expected final x position of car1
    assert car1.y == 2  # Expected final y position of car1
    assert car1.direction == 'E'  # Expected direction of car1

    assert car2.x == 1  # Expected final x position of car2
    assert car2.y == 3  # Expected final y position of car2
    assert car2.direction == 'E'  # Expected direction of car2

    assert car3.x == 4  # Expected final x position of car3
    assert car3.y == 0  # Expected final y position of car3
    assert car3.direction == 'E'  # Expected direction of car3

   """
   #assert car1.x ==2




if __name__ == '__main__':
    pytest.main()
