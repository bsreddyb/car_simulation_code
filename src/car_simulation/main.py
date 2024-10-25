# main.py

from simulation.simulation import Simulation
from simulation.field import Field
from simulation.car import Car
from typing import Tuple
from localize.localize import localizations
from utils.logger import Logger
from config.config import Config

class Main:

    logger = Logger.setup_logger('MAIN')
    def start(self) -> None:
        """
        Prompts the user to input the dimensions of the field and returns a Field object.
        Field -> The field object with the specified dimensions.
        """
       # print("Welcome to Auto Driving Car Simulation!")
        print(localizations.get('start_message', 'Welcome!'))  # Use .get() for safety
        width, height = self.create_field()
        field = Field(width, height)
        simulation = Simulation(field)
        while True:
            print("\nPlease choose from the following options:")
            print("[1] Add a car to field")
            print("[2] Run simulation")
            choice = input().strip()

            if choice == '1':
                try:
                    car = self.create_car()
                    simulation.add_car(car)
                    simulation.print_car_list()
                except Exception as e:
                    print(f"Error adding car: {e}")
            elif choice == '2':
                try:
                    simulation.run_simulation()
                    exit_choice = self.post_simulation_menu(simulation)
                    if exit_choice:  # If user chose to exit
                        break
                except Exception as e:
                    print(f"Error running simulation: {e}")

    def create_field(self) -> Tuple[int, int]:
        """
        User prompted to input the dimensions of the field and returns a Field object.
        Returns: Field
        The field object with the specified dimensions.
        """
        while True:
            try:
                width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
                print(f"You have created a field of {width} x {height}.")
                return width, height
            except ValueError:
                print("Invalid input. Please enter two integers separated by a space.")
    
    def create_car(self) -> Car:
        """
        Prompts the user to input the dimensions of the field and returns a Field object.
        Returns:
        --------
        Car
        The Car object with initial position and direction.
        """
        DIRECTIONS = Config.CAR_DIRECTIONS
        COMMANDS = Config.CAR_COMMANDS
        
        while True:
            try:
                name = input("Please enter the name of the car: ")

                # Loop for getting the initial position and direction
                while True:
                    position_input = input(f"Please enter the initial position of car {name} in x y Direction format ")
                    parts = position_input.split()

                    if len(parts) != 3:
                        print("Invalid input. Please enter in the format 'x y Direction'.")
                        continue  # Ask for input again

                    try:
                        x, y = int(parts[0]), int(parts[1])
                        direction = parts[2].upper()
                    except ValueError:
                        print("Invalid input. Please ensure you enter numeric values for x and y.")
                        continue  # Ask for input again

                    # Validate direction
                    if direction not in DIRECTIONS:
                        print(Config.INVALID_DIRECTION_MESSAGE)
                        continue  # Ask for direction input again

                    break  # Exit the direction loop if input is valid

                # Loop for getting commands for the car
                while True:
                    commands = input(f"Please enter the commands for car {name} : ").strip().upper()

                    if all(command in COMMANDS for command in commands):
                        break  # Exit command loop if all commands are valid
                    else:
                        print(Config.INVALID_COMMAND_MESSAGE)

                return Car(name, x, y, direction, commands)  # Create and return the Car object
            except Exception as e:
                print(f"Error creating car: {e}")


    def post_simulation_menu(self, simulation: Simulation) -> bool:
        while True:
            print("\nPlease choose from the following options:")
            print("[1] Start over")
            print("[2] Exit")
            choice = input()
            
            if choice == '1':
                return False  # Indicates to start over
            elif choice == '2':
                print("Thank you for running the simulation. Goodbye!")
                return True  # Indicates to exit
            else:
                print("Invalid choice. Please enter 1 or 2.")

if __name__ == '__main__':
    main = Main()
    main.start()
