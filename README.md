## Auto Driving Car Simulation

# Overview
A simulation program for grid-based autonomous vehicle driving. In addition to adding vehicles and issuing commands, users may also simulate movement with boundary limits and collision detection.

## Features
Add vehicles with distinctive names to a simulation.
-To control each car's motion, set commands for it.
-Launch the simulation and watch the cars' ultimate locations and orientations.
-Identify and report vehicle-boundary collisions.
#Requirements

#Installation

#Usage


#Running Tests

Project Structure
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
  - unit/
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
