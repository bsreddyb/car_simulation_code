class Config:
    # Logging configuration
    LOGGING_LEVEL = 'INFO'
    LOGGING_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    # Default localization
    DEFAULT_LOCALIZATION_LANGUAGE = 'en'
    # Static arrays for directions and commands
    CAR_DIRECTIONS = ['N','E','S','W']
    CAR_COMMANDS = ['L','R','F']
    INVALID_DIRECTION_MESSAGE = "Invalid direction. Please enter N, S, E, or W."
    INVALID_COMMAND_MESSAGE = "Invalid commands. Please enter only L, R, F."
        

