# simulation/simulation.py

from typing import List
from .car import Car  # Correct relative import
from .field import Field  # Correct relative import
from car_simulation.utils.logger import Logger
class Simulation:

    """
        This class represents the simulation of cars on a field.

        Attributes:
            field : Field -> The field on which the simulation runs.
            cars : list   -> The list of cars in the simulation.
            stopped_cars : set  -> The set of cars that have stopped.
            collisions : List The collisions messages 
            
    """
    def __init__(self, field: Field):
        self.field: Field = field
        self.cars: List[Car] = []
        self.collisions: List[str] = []  # Store collision messages
        self.stopped_cars = set()     
        self.boundary_collisions = set()
        self.logger = Logger.setup_logger('Simulation')

    def add_car(self, car: Car) -> None:
        """Add a car to the simulation.
        try:
            self.cars.append(car)
            print(f"{car.name} added to the simulation.")
        except Exception as e:
            print(f"Error adding car {car.name}: {e}")
            """
        """Add a car to the simulation with bounds checking."""
        if not self.field.within_bounds(car.x, car.y):
            raise ValueError("Car position is out of bounds")
        self.cars.append(car)
        print(f"{car.name} added to the simulation.")

    def print_car_list(self) -> None:
        """Print the list of cars in the simulation."""
        print("Your current list of cars are:")
        for car in self.cars:
            print(f"- {car}")


    def check_collision(self, step: int) -> None:
        """Check if any cars have collided and deactivate them."""
        try:
            positions = {}
            for car in self.cars:
                if car.active:
                    pos = (car.x, car.y)
                    if pos in positions:
                        # Collision detected
                        collision_msg_a = f"{car.name} collides with {positions[pos].name} at ({pos[0]},{pos[1]}) at step {step}"
                        collision_msg_b = f"{positions[pos].name} collides with {car.name} at ({pos[0]},{pos[1]}) at step {step}"
                        self.collisions.append(collision_msg_a)
                        self.collisions.append(collision_msg_b)
                        car.active = False
                        positions[pos].active = False
                    else:
                        positions[pos] = car
        except Exception as e:
            print(f"Error checking collisions at step {step}: {e}")

    def run_simulation(self) -> None:
        """Run the simulation step-by-step, executing each car's commands."""
        try:
            max_steps = max(len(car.commands) for car in self.cars) if self.cars else 0
            for step in range(max_steps):
                for car in self.cars:
                    car.execute_command(self.field)
                self.check_collision(step)
            self.print_results()
            
        except Exception as e:
            print(f"Error during simulation: {e}")

    def print_results(self) -> None:
        """Print the final positions of all cars after simulation."""
        print("\nAfter simulation, the result is:")
        for car in self.cars:
            if car.active:
                print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")
            else:
                print(f"- {car.name} is no longer active due to collision.")

        # Print all collision messages if any
        for collision in self.collisions:
            print(collision)
    
    def is_out_of_bounds(self, car):
        # Implement boundary logic
        # Example:
        return car.y < 0 or car.y >= grid_height  # Adjust grid_height accordingly
    
    def reset(self):
        self.cars = []
        self.boundary_collisions.clear()
        self.stopped_cars.clear()
        self.collisions.clear()
