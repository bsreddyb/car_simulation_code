## Auto Driving Car Simulation

# Overview
A simulation program for grid-based autonomous vehicle driving. In addition to adding vehicles and issuing commands, users may also simulate movement with boundary limits and collision detection.

## Features
Add vehicles with distinctive names to a simulation.
-To control each car's motion, set commands for it.
-Launch the simulation and watch the cars' ultimate locations and orientations.
-Identify and report vehicle-boundary collisions.

##Requirements
Python 3.9+
pytest for running tests

##Installation
  #Clone the repository:
    git clone https://github.com/bsreddyb/car_simulation.git
    cd car-simulation
  
  #Create a Virtual Environment (Optional):
    Make sure Python is installed on your computer. To keep dependencies structured and distinct from other projects, a virtual environment is advised.
  ```
      # Create a virtual environment (optional)
      python -m venv venv
      # Activate the virtual environment
      # On Windows
      venv\Scripts\activate
      # On MacOS/Linux
      source venv/bin/activate

# Install the package
pip install .

  ```
  ##Usage
  # Create a virtual environment (optional)
  ```
  python -m venv venv
  ```
  # Activate the virtual environment
  # On Windows
  ```
  venv\Scripts\activate
  ```
  # On MacOS/Linux
  ```
  source venv/bin/activate
  ```
# Install the package
Installing the auto_driving_car_simulation package with pip is possible once you are in the virtual or global environment of your choice. Additionally, this will install all required dependencies:
```
pip install .
```
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
