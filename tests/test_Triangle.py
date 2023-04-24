import pytest
from scr.Triangle import Triangle


class TestTriangle:

    @pytest.mark.parametrize('ab, bc, ac, expected_perimeter, expected_area',
                             [
                                 (3, 4, 5, 12, 6),
                                 (5, 5, 8, 18, 12),
                                 (9, 9, 9, 27, 35.1)
                             ])
    def test_positive_creating(self, ab, bc, ac, expected_perimeter, expected_area):
        triangle = Triangle(ab, bc, ac)
        assert triangle.get_perimeter() == expected_perimeter
        assert triangle.get_area() == expected_area


    @pytest.mark.parametrize('ab, bc, ac',
                             [
                                 (3, -4, 5), (-5, 5, 8), (9, 9, -9), (-3, -4, -5)
                             ])
    def test_dont_create_negative_side(self, ab, bc, ac):
        with pytest.raises(ValueError):
            Triangle(ab, bc, ac)

    @pytest.mark.parametrize('ab, bc, ac',
                             [
                                 (0, 4, 5),(5, 0, 8), (9, 9, 0), (0, 0, 0)
                             ])
    def test_dont_create_null_side(self, ab, bc, ac):
        with pytest.raises(ValueError):
            Triangle(ab, bc, ac)

    @pytest.mark.parametrize('ab, bc, ac',
                             [
                                (None, 4, 5),(5, None, 8), (9, 9, None), (None, None, None)
                              ])
    def test_dont_create_none_side(self, ab, bc, ac):
        with pytest.raises(TypeError):
            Triangle(ab, bc, ac)

    @pytest.mark.parametrize('ab, bc, ac',
                             [
                                ('str', 4, 5),(5, 'str', 8), (9, 9, 'str'),('str', 'int', 'float')

                              ])
    def test_dont_create_str_side(self, ab, bc, ac):
        with pytest.raises(TypeError):
            Triangle(ab, bc, ac)