# simulation/field.py

class Field:
    def __init__(self, width: int, height: int):
        """
        A class which represents the field in the simulation with below attributes   
        width : int ->The width of the field.
        height : int -> The height of the field.
        """
        self.width = width
        self.height = height

    def within_bounds(self, x: int, y: int) -> bool:
        """Check if the given position (x, y) is within the field's boundaries.        Parameters:
        -----------
        x : int -> The x-coordinate to check.
        y : int -> The y-coordinate to check.

        Returns:
            bool-> True if the coordinates are within boundaries, otherwise False.
        """
        return 0 <= x < self.width and 0 <= y < self.height
