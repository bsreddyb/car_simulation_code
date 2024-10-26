## Auto Driving Car Simulation

## Overview
A simulation program for grid-based autonomous vehicle driving. In addition to adding vehicles and issuing commands, users may also simulate movement with boundary limits and collision detection.

## Features
Add vehicles with distinctive names to a simulation.
-To control each car's motion, set commands for it.
-Launch the simulation and watch the cars' ultimate locations and orientations.
-Identify and report vehicle-boundary collisions.

## Requirements
Python 3.9+
pytest for running tests

## Installation
  #1 Clone the repository:
      ```
        git clone https://github.com/bsreddyb/car_simulation.git
        cd car-simulation
      ```  
  #2 Create a Virtual Environment (Optional):
    Make sure Python is installed on your computer. To keep dependencies structured and distinct from other projects, a 
    virtual environment is advised.
      ```
          # Create a virtual environment (optional)
          python -m venv venv
          # Activate the virtual environment
          # On Windows
          venv\Scripts\activate
          # On MacOS/Linux
          source venv/bin/activate
     ```
  #3 Install the package
Once you are in the virtual or global environment of your choice, you can use pip to install the car_simulation package. Additionally, all required dependencies will be installed:
     ```
       pip install .
     ```
##Usage
Use the following command to launch the simulation:
    ```
    run-simulation
    ``~
Set up the field, add cars and launch the simulation by following the on-screen directions.

##Running Tests
To run the tests, use pytest:
    ```
        python -m pytest    
    ```
###Project Structure
- src/: Contains the simulation source code.
  - car_simulation/
    - main.py: The main entry point for starting the simulation.
    - simulation/
      - car.py: Defines the Car class.
      - field.py: Defines the Field class.
      - simulation.py: Defines the Simulation class.
    - localize/
      - localize.py: Handles localization.
      - en.yaml: Contains English localization strings.
    - config/
      - config.py: Contains configuration settings.
    - utils/
      - logger.py: Sets up logging.
- tests/: Contains the test cases for the project.
  -unit/
    - test_car.py: Tests for the Car class.
    - test_field.py: Tests for the Field class.
    - test_simulation.py: Tests for the Simulation class.
  - integration/
    - test_main_integration.py: Integration tests for the main.py functions.
    - test_simulation_integration.py: Integration tests for the Simulation - setup.py: Script for setting up the package.
- README.md: Project documentation.
- MANIFEST.in: Specifies additional files to include in the package.
- requirements.txt: Lists the dependencies for the project.

Assumptions
*If an invalid input is entered, the application will prompt for correct inputs.
*The car's name must be distinct and required.
*The name of the car must be a string with a minimum of one character.
*If a new coordinate is detected that is outside the designated field size or collides with another car, stop driving.
