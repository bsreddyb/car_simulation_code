import pytest
from unittest.mock import patch, MagicMock
from src.car_simulation.main import Main
from src.car_simulation.simulation.car import Car
from src.car_simulation.simulation.field import Field
from src.car_simulation.simulation.simulation import Simulation

class TestMain:
    
    @patch('builtins.input', side_effect=["10 10"])
    def test_create_field(self, mock_input):
        main = Main()
        width, height = main.create_field()
        assert width == 10
        assert height == 10
        mock_input.assert_called_once()

    @patch('builtins.input', side_effect=["Invalid", "5 5"])
    def test_create_field_invalid_then_valid(self, mock_input):
        main = Main()
        width, height = main.create_field()
        assert width == 5
        assert height == 5
        assert mock_input.call_count == 2  # Called twice, once for invalid input

    @patch('builtins.input', side_effect=["Car1", "0 0 N", "FRL"])
    def test_create_car(self, mock_input):
        main = Main()
        car = main.create_car()
        assert isinstance(car, Car)
        assert car.name == "Car1"
        assert car.x == 0
        assert car.y == 0
        assert car.direction == "N"
        assert car.commands == "FRL"
        assert mock_input.call_count == 3

    @patch('builtins.input', side_effect=["Car1", "invalid", "0 0 N", "invalid commands", "FRL"])
    def test_create_car_with_invalid_inputs(self, mock_input):
        main = Main()
        car = main.create_car()
        assert isinstance(car, Car)
        assert car.name == "Car1"
        assert car.x == 0
        assert car.y == 0
        assert car.direction == "N"
        assert car.commands == "FRL"
        assert mock_input.call_count == 5  # Handling invalid inputs

    @patch('builtins.input', side_effect=["1", "Car1", "0 0 N", "FRL", "2", "2"])
    @patch('src.car_simulation.simulation.simulation.Simulation.run_simulation')
    @patch('src.car_simulation.simulation.simulation.Simulation.add_car')
    @patch('src.car_simulation.simulation.simulation.Simulation.print_car_list')
    def test_start_add_car_then_simulation(self, mock_print_list, mock_add_car, mock_run_simulation, mock_input):
        main = Main()
        main.create_field = MagicMock(return_value=(5, 5))  # Mock field creation
        car = Car("Car1", 0, 0, "N", "FRL")
        main.create_car = MagicMock(return_value=car)  # Mock car creation

        main.start()  # Running the start process

        # Assertions for calls to respective methods
        mock_add_car.assert_called_once_with(car)
        mock_print_list.assert_called_once()
        mock_run_simulation.assert_called_once()
        assert mock_input.call_count == 6

    @patch('builtins.input', side_effect=["2", "1"])
    def test_post_simulation_menu_exit(self, mock_input):
        main = Main()
        simulation = MagicMock()
        should_exit = main.post_simulation_menu(simulation)
        assert should_exit is True
        assert mock_input.call_count == 2

    @patch('builtins.input', side_effect=["1", "2"])
    def test_post_simulation_menu_restart(self, mock_input):
        main = Main()
        simulation = MagicMock()
        should_exit = main.post_simulation_menu(simulation)
        assert should_exit is False
        assert mock_input.call_count == 2
