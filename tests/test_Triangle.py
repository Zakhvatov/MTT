import pytest
from scr.Triangle import Triangle


class TestTriangle:
    @pytest.mark.parametrize('ab, bc, ac, expected_perimeter, expected_area',
                             [
                                 (3, 4, 5, 12, 6),
                                 (5, 5, 8, 18, 12),
                                 (9, 9, 9, 27, 35)
                             ])
    def test_positive_creating(self, ab, bc, ac, expected_perimeter, expected_area):
        triangle = Triangle(ab, bc, ac)
        j = triangle.get_perimeter()
        assert triangle.get_perimeter() == expected_perimeter
        assert triangle.get_area() == expected_area
