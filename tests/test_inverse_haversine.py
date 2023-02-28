from haversine import inverse_haversine, haversine, Unit, Direction
from numpy import isclose
from math import pi
import pytest

from tests.geo_ressources import LYON, PARIS, NEW_YORK, LONDON


@pytest.mark.parametrize(
    "point, dir, dist, result",
    [
        (PARIS, Direction.NORTH, 32, (49.144444, 2.3508)),
        (PARIS, 0, 32, (49.144444, 2.3508)),
        (LONDON, Direction.WEST, 50, (51.507778, -0.840556)),
        (LONDON, pi * 1.5, 50, (51.507778, -0.840556)),
        (NEW_YORK, Direction.SOUTH, 15, (40.568611, -74.235278)),
        (NEW_YORK, Direction.NORTHWEST, 50, (41.020556, -74.656667)),
        (NEW_YORK, pi * 1.25, 50, (40.384722, -74.6525)),
    ],
)
def test_inverse_kilometers(point, dir, dist, result):
    assert isclose(inverse_haversine(point, dist, dir),
                   result, rtol=1e-5).all()


@pytest.mark.parametrize(
    "point, direction, distance, unit",
    [
        (PARIS, Direction.NORTH, 10, Unit.KILOMETERS),
        (LONDON, Direction.WEST, 32, Unit.MILES),
        (LYON, Direction.NORTHEAST, 45_000, Unit.METERS),
        (NEW_YORK, Direction.SOUTH, 15, Unit.NAUTICAL_MILES),
    ],
)
def test_back_and_forth(point, direction, distance, unit):
    new_point = inverse_haversine(point, distance, direction, unit)
    assert isclose(haversine(new_point, point, unit), distance, rtol=1e-10)


def test_inverse_miles():
    assert isclose(inverse_haversine(PARIS, 50, Direction.NORTH,
                   unit=Unit.MILES), (49.5803579218996, 2.3508), rtol=1e-5).all()


def test_nautical_inverse_miles():
    assert isclose(inverse_haversine(PARIS, 10, Direction.SOUTH,
                   unit=Unit.NAUTICAL_MILES), (48.69014586638915, 2.3508), rtol=1e-5).all()


@pytest.mark.parametrize(
    "point, direction, distance, unit, expected",
    [
        (PARIS, Direction.WEST, 3000, Unit.KILOMETERS, (PARIS[0], 0)),
        # (LYON, Direction.WEST, 3000, Unit.KILOMETERS, (LYON[0], 0)),
    ],
)
def test_explicit_cardinal_points(point, direction, distance, unit, expected):
    """
    Test going north/south should not alter latitude and going east/west should not alter longitude
    """
    assert inverse_haversine(point, distance, direction, unit)[
        0] == expected[0]
