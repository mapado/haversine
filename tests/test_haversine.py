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


@pytest.mark.parametrize(
    "oob_from,oob_to,proper_from,proper_to", [
        ((-90.0001, 0), (0, 0), (-89.9999, 180), (0, 0)),
        ((-90.0001, 30), (0, 0), (-89.9999, -150), (0, 0)),
        ((0, 0), (90.0001, 0), (0, 0), (89.9999, -180)),
        ((0, 0), (90.0001, 30), (0, 0), (89.9999, -150)),
        ((0, -180.0001), (0, 0), (0, 179.9999), (0, 0)),
        ((30, -180.0001), (0, 0), (30, 179.9999), (0, 0)),
        ((0, 0), (0, 180.0001), (0, 0), (0, -179.9999)),
        ((0, 0), (30, 180.0001), (0, 0), (30, -179.9999)),
    ]
)
def test_normalization(oob_from, oob_to, proper_from, proper_to):
    """
    Test makes sure that normalization works as expected by comparing distance of out of
    bounds points cases to equal cases where all points are within lat/lon ranges. The
    results are expected to be equal (within some tolerance to account for numerical
    issues).
    """
    normalized_during, normalized_already = (
        haversine(oob_from, oob_to, Unit.DEGREES, normalize=True),
        haversine(proper_from, proper_to, Unit.DEGREES, normalize=True),
    )
    assert normalized_during == pytest.approx(normalized_already, abs=1e-10)


@pytest.mark.parametrize(
    "oob_from,oob_to", [
        ((-90.0001, 0), (0, 0)),
        ((0, 0), (90.0001, 0)),
        ((0, -180.0001), (0, 0)),
        ((0, 0), (0, 180.0001)),
    ]
)
def test_out_of_bounds(oob_from, oob_to):
    """
    Test makes sure that a ValueError is raised when latitude or longitude values are out of bounds.
    """
    with pytest.raises(ValueError):
        haversine(oob_from, oob_to)
    with pytest.raises(ValueError):
        haversine(oob_from, oob_to, normalize=False)


@pytest.mark.parametrize(
    "in_bounds_from,in_bounds_to", [
        ((-90, 0), (0, 0)),
        ((0, 0), (90, 0)),
        ((0, -180), (0, 0)),
        ((0, 0), (0, 180)),
    ]
)
def test_in_bounds(in_bounds_from, in_bounds_to):
    """
    Test makes sure that a ValueError is NOT raised when latitude or longitude values are in bounds.
    """
    assert haversine(in_bounds_from, in_bounds_to) > 0


def test_haversine_deg_rad_great_circle_distance():
    """
    Test makes sure the haversine functions returns the great circle distance (https://en.wikipedia.org/wiki/Great-circle_distance) between two points on a sphere.
    See https://github.com/mapado/haversine/issues/45
    """
    p1, p2 = (0, -45), (0, 45)
    assert haversine(p1, p2, Unit.DEGREES) == 89.99999999999997
