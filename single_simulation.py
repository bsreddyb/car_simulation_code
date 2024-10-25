from typing import List, Tuple, Optional


class Field:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def within_bounds(self, x: int, y: int) -> bool:
        """Check if the given position (x, y) is within the field's boundaries."""
        return 0 <= x < self.width and 0 <= y < self.height


class Car:
    DIRECTIONS = ['N', 'E', 'S', 'W']  # North, East, South, West

    def __init__(self, name: str, x: int, y: int, direction: str, commands: str):
        self.name: str = name
        self.x: int = x
        self.y: int = y
        self.direction: str = direction
        self.commands: str = commands
        self.command_index: int = 0
        self.active: bool = True  # Set to False if the car stops (collision, etc.)

    def turn_left(self) -> None:
        current_index = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_index - 1) % 4]

    def turn_right(self) -> None:
        current_index = Car.DIRECTIONS.index(self.direction)
        self.direction = Car.DIRECTIONS[(current_index + 1) % 4]

    def move_forward(self, field: Field) -> None:
        """Move forward by one unit in the current direction if within bounds."""
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

    def next_command(self) -> Optional[str]:
        """Return the next command to execute, or None if commands are exhausted."""
        if self.command_index < len(self.commands):
            return self.commands[self.command_index]
        return None

    def execute_command(self, field: Field) -> None:
        if not self.active:
            return
        command = self.next_command()
        if command == 'L':
            self.turn_left()
        elif command == 'R':
            self.turn_right()
        elif command == 'F':
            self.move_forward(field)
        self.command_index += 1

    def __repr__(self) -> str:
        return f"{self.name}, ({self.x},{self.y}) {self.direction}, {self.commands}"


class Simulation:
    def __init__(self, field: Field):
        self.field: Field = field
        self.cars: List[Car] = []

    def add_car(self, car: Car) -> None:
        self.cars.append(car)

    def print_car_list(self) -> None:
        print("Your current list of cars are:")
        for car in self.cars:
            print(f"- {car}")

    def check_collision(self) -> None:
        """Check if any cars have collided and deactivate them."""
        positions = {}
        for car in self.cars:
            if car.active:
                pos = (car.x, car.y)
                if pos in positions:
                    # Collision detected
                    print(f"{car.name} collides with {positions[pos].name} at {pos}")
                    car.active = False
                    positions[pos].active = False
                else:
                    positions[pos] = car

    def run_simulation(self) -> None:
        """Run the simulation step-by-step, executing each car's commands."""
        max_steps = max(len(car.commands) for car in self.cars)
        for _ in range(max_steps):
            for car in self.cars:
                car.execute_command(self.field)
            self.check_collision()
        self.print_results()

    def print_results(self) -> None:
        """Print the final positions of all cars after simulation."""
        print("\nAfter simulation, the result is:")
        for car in self.cars:
            print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")


class Main:
    def start(self) -> None:
        print("Welcome to Auto Driving Car Simulation!")
        width, height = self.create_field()
        field = Field(width, height)
        simulation = Simulation(field)
        
        while True:
            print("\nPlease choose from the following options:")
            print("[1] Add a car to field")
            print("[2] Run simulation")
            choice = input().strip()

            if choice == '1':
                car = self.create_car()
                simulation.add_car(car)
                simulation.print_car_list()
            elif choice == '2':
                simulation.run_simulation()
                self.post_simulation_menu(simulation)

    def create_field(self) -> Tuple[int, int]:
        width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
        print(f"You have created a field of {width} x {height}.")
        return width, height

    def create_car(self) -> Car:
        name = input("Please enter the name of the car: ")
        x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
        x, y = int(x), int(y)
        commands = input(f"Please enter the commands for car {name}: ").strip().upper()
        return Car(name, x, y, direction, commands)

    def post_simulation_menu(self, simulation: Simulation) -> None:
        print("\nPlease choose from the following options:")
        print("[1] Start over")
        print("[2] Exit")
        choice = input().strip()

        if choice == '1':
            self.start()  # Restart the simulation
        elif choice == '2':
            print("Thank you for running the simulation. Goodbye!")
            return True  # Indicates to exit
        else:
            print("Invalid choice. Please enter 1 or 2.")


if __name__ == '__main__':
    main = Main()
    main.start()
