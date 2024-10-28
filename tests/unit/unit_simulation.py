import pytest
from unittest.mock import MagicMock
from src.car_simulation.simulation.simulation import Simulation
from src.car_simulation.simulation.car import Car
from src.car_simulation.simulation.field import Field


@pytest.fixture
def simulation():
    # Create a mock field with specific boundaries
    field = MagicMock(spec=Field)
    field.within_bounds.return_value = True  # Default to within bounds for tests
    return Simulation(field)

def test_initialization(simulation):
    """Test if simulation initializes correctly."""
    assert simulation.cars == []
    assert simulation.collisions == []
    assert simulation.logger is not None

def test_add_car_within_bounds(simulation):
    """Test adding a car within bounds."""
    car = Car(name="TestCar", x=0, y=0, direction="N", commands=[])
    simulation.add_car(car)
    assert car in simulation.cars

def test_add_car_out_of_bounds(simulation):
    """Test adding a car out of bounds raises ValueError."""
    car = Car(name="OutOfBoundCar", x=-1, y=0, direction="N", commands=[])
    simulation.field.within_bounds.return_value = False  # Simulate out of bounds
    with pytest.raises(ValueError):
        simulation.add_car(car)

def test_check_collision(simulation):
    """Test that collisions are detected."""
    car1 = Car(name="Car1", x=1, y=1, direction="N", commands=[])
    car2 = Car(name="Car2", x=1, y=1, direction="N", commands=[])
    simulation.add_car(car1)
    simulation.add_car(car2)

    simulation.check_collision(step=0)

    assert "Car1 collides with Car2 at (1,1) at step 0" in simulation.collisions
    assert "Car2 collides with Car1 at (1,1) at step 0" in simulation.collisions
    assert not car1.active
    assert not car2.active

def test_run_simulation(simulation):
    """Test running the simulation and executing commands."""
    car = Car(name="TestCar", x=0, y=0, direction="N", commands=["F"])
    simulation.add_car(car)

    # Mock the execute_command method to update the position
    car.execute_command = MagicMock(side_effect=lambda field: setattr(car, 'y', 1))

    simulation.run_simulation()

    assert car.y == 1  # Check if the car has moved forward
    assert car.active  # The car should still be active

def test_print_car_list(simulation, capsys):
    """Test printing the list of cars."""
    car1 = Car(name="Car1", x=0, y=0, direction="N", commands=[])
    car2 = Car(name="Car2", x=1, y=1, direction="N", commands=[])
    simulation.add_car(car1)
    simulation.add_car(car2)

    # Capture the print output
    simulation.print_car_list()

    # Check the captured output
    captured = capsys.readouterr()
    assert "Your current list of cars are:" in captured.out
    assert "Car1" in captured.out
    assert "Car2" in captured.out

def test_reset_functionality(simulation):
    """Test that reset clears cars and collisions."""
    car = Car(name="TestCar", x=0, y=0, direction="N", commands=[])
    simulation.add_car(car)
    simulation.collisions.append("Collision occurred")

    simulation.reset()

    assert simulation.cars == []
    assert simulation.collisions == []
    assert simulation.boundary_collisions == set()
    assert simulation.stopped_cars == set()

if __name__ == '__main__':
    pytest.main()
