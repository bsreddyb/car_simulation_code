import pytest
from src.car_simulation.simulation.field import Field

class TestField:
    
    def test_field_initialization(self):
        """
        Test the initialization of the Field class.
        """
        field = Field(10, 5)
        assert field.width == 10
        assert field.height == 5

    @pytest.mark.parametrize("x, y, expected", [
        (0, 0, True),   # Edge case: top-left corner
        (9, 4, True),   # Edge case: bottom-right corner
        (5, 2, True),   # Inside the field
        (-1, 0, False), # Out of bounds: negative x
        (0, -1, False), # Out of bounds: negative y
        (10, 4, False), # Out of bounds: x too large
        (9, 5, False)   # Out of bounds: y too large
    ])
    def test_within_bounds(self, x, y, expected):
        """
        Test the within_bounds method for various cases.
        """
        field = Field(10, 5)
        assert field.within_bounds(x, y) == expected
