from haversine import haversine, Unit
from math import pi
import pytest

from tests.geo_ressources import LYON, PARIS, NEW_YORK, LONDON, EXPECTED_LYON_PARIS

def haversine_test_factory(unit):
    def test():
        expected = EXPECTED_LYON_PARIS[unit]
        assert haversine(LYON, PARIS, unit=unit) == expected
        assert isinstance(unit.value, str)
        assert haversine(LYON, PARIS, unit=unit.value) == expected

    return test


test_kilometers = haversine_test_factory(Unit.KILOMETERS)
test_meters = haversine_test_factory(Unit.METERS)
test_miles = haversine_test_factory(Unit.MILES)
test_nautical_miles = haversine_test_factory(Unit.NAUTICAL_MILES)
test_feet = haversine_test_factory(Unit.FEET)
test_inches = haversine_test_factory(Unit.INCHES)
test_radians = haversine_test_factory(Unit.RADIANS)
test_degrees = haversine_test_factory(Unit.DEGREES)


def test_units_enum():
    from haversine.haversine import _CONVERSIONS
    assert all(unit in _CONVERSIONS for unit in Unit)


def test_haversine_deg_rad():
    """
    Test makes sure that one time around earth matches sphere circumference in degrees / radians.
    """
    p1, p2 = (45, 0), (-45, 180)
    assert haversine(p1, p2, unit=Unit.RADIANS) == pi
    assert round(haversine(p1, p2, unit=Unit.DEGREES), 13) == 180.0


def test_normalization():
    """
    Test makes sure that latitude values outside of [-90,90] and longitude values outside of [-180,180] are normalized into their ranges.
    """
    normalized, straight = (
        haversine((-90.0001, 0), (0, 0), Unit.DEGREES, normalize=True),
        haversine((-89.9999, 180), (0, 0), Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine((-90.0001, 30), (0, 0), Unit.DEGREES, normalize=True),
        haversine((-89.9999, -150), (0, 0), Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine((0, 0), (90.0001, 0), Unit.DEGREES, normalize=True),
        haversine((0, 0), (89.9999, -180), Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine((0, 0), (90.0001, 30), Unit.DEGREES, normalize=True),
        haversine((0, 0), (89.9999, -150), Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine((0, -180.0001), (0, 0), Unit.DEGREES, normalize=True),
        haversine((0, 179.9999), (0, 0), Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine((30, -180.0001), (0, 0), Unit.DEGREES, normalize=True),
        haversine((30, 179.9999), (0, 0), Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine((0, 0), (0, 180.0001), Unit.DEGREES, normalize=True),
        haversine((0, 0), (0, -179.9999), Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine((0, 0), (30, 180.0001), Unit.DEGREES, normalize=True),
        haversine((0, 0), (30, -179.9999), Unit.DEGREES, normalize=True),
    )
    assert normalized == straight


def test_out_of_bounds():
    """
    Test makes sure that a ValueError is raised when latitude or longitude values are out of bounds.
    """
    with pytest.raises(ValueError):
        haversine((-90.0001, 0), (0, 0))
    with pytest.raises(ValueError):
        haversine((0, 0), (90.0001, 0))
    with pytest.raises(ValueError):
        haversine((0, -180.0001), (0, 0))
    with pytest.raises(ValueError):
        haversine((0, 0), (0, 180.0001))
    with pytest.raises(ValueError):
        haversine((-90.0001, 0), (0, 0), normalize=False)
    with pytest.raises(ValueError):
        haversine((0, 0), (90.0001, 0), normalize=False)
    with pytest.raises(ValueError):
        haversine((0, -180.0001), (0, 0), normalize=False)
    with pytest.raises(ValueError):
        haversine((0, 0), (0, 180.0001), normalize=False)


def test_haversine_deg_rad_great_circle_distance():
    """
    Test makes sure the haversine functions returns the great circle distance (https://en.wikipedia.org/wiki/Great-circle_distance) between two points on a sphere.
    See https://github.com/mapado/haversine/issues/45
    """
    p1, p2 = (0, -45), (0, 45)
    assert haversine(p1, p2, Unit.DEGREES) == 89.99999999999997
