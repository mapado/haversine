from haversine import haversine_vector, Unit
from numpy.testing import assert_allclose
import pytest

from tests.geo_ressources import EXPECTED_LONDON_PARIS, EXPECTED_LYON_NEW_YORK, EXPECTED_LYON_PARIS, EXPECTED_LONDON_NEW_YORK, LYON, PARIS, NEW_YORK, LONDON

@pytest.mark.parametrize(
    'unit', [Unit.KILOMETERS, Unit.METERS, Unit.INCHES]
)
def test_pair(unit):
    def test_lyon_paris(unit):
        expected_lyon_paris = EXPECTED_LYON_PARIS[unit]
        assert haversine_vector(LYON, PARIS, unit=unit) == expected_lyon_paris
        assert isinstance(unit.value, str)
        assert haversine_vector(LYON, PARIS, unit=unit.value) == expected_lyon_paris

    return test_lyon_paris(unit)


def test_normalization():
    """
    Test makes sure that latitude values outside of [-90,90] and longitude values outside of [-180,180] are normalized into their ranges.
    """
    normalized, straight = (
        haversine_vector([(-90.0001, 0)], [(0, 0)], Unit.DEGREES, normalize=True),
        haversine_vector([(-89.9999, 180)], [(0, 0)], Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine_vector([(-90.0001, 30)], [(0, 0)], Unit.DEGREES, normalize=True),
        haversine_vector([(-89.9999, -150)], [(0, 0)], Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine_vector([(0, 0)], [(90.0001, 0)], Unit.DEGREES, normalize=True),
        haversine_vector([(0, 0)], [(89.9999, -180)], Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine_vector([(0, 0)], [(90.0001, 30)], Unit.DEGREES, normalize=True),
        haversine_vector([(0, 0)], [(89.9999, -150)], Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine_vector([(0, -180.0001)], [(0, 0)], Unit.DEGREES, normalize=True),
        haversine_vector([(0, 179.9999)], [(0, 0)], Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine_vector([(30, -180.0001)], [(0, 0)], Unit.DEGREES, normalize=True),
        haversine_vector([(30, 179.9999)], [(0, 0)], Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine_vector([(0, 0)], [(0, 180.0001)], Unit.DEGREES, normalize=True),
        haversine_vector([(0, 0)], [(0, -179.9999)], Unit.DEGREES, normalize=True),
    )
    assert normalized == straight
    normalized, straight = (
        haversine_vector([(0, 0)], [(30, 180.0001)], Unit.DEGREES, normalize=True),
        haversine_vector([(0, 0)], [(30, -179.9999)], Unit.DEGREES, normalize=True),
    )
    assert normalized == straight


def test_out_of_bounds():
    """
    Test makes sure that a ValueError is raised when latitude or longitude values are out of bounds.
    """
    with pytest.raises(ValueError):
        haversine_vector([(-90.0001, 0)], [(0, 0)], Unit.DEGREES, normalize=False)
    with pytest.raises(ValueError):
        haversine_vector([(0, 0)], [(90.0001, 0)], Unit.DEGREES, normalize=False)
    with pytest.raises(ValueError):
        haversine_vector([(0, -180.0001)], [(0, 0)], Unit.DEGREES, normalize=False)
    with pytest.raises(ValueError):
        haversine_vector([(0, 0)], [(0, 180.0001)], Unit.DEGREES, normalize=False)


def test_haversine_vector_comb():
    unit = Unit.KILOMETERS
    expected = [
        [EXPECTED_LYON_PARIS[unit],  EXPECTED_LONDON_PARIS[unit]],
        [EXPECTED_LYON_NEW_YORK[unit], EXPECTED_LONDON_NEW_YORK[unit]]
    ]

    assert_allclose( # See https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose
        haversine_vector([LYON, LONDON], [PARIS, NEW_YORK], unit, comb=True),
        expected
    )

def test_units_enum():
    from haversine.haversine import _CONVERSIONS
    assert all(unit in _CONVERSIONS for unit in Unit)
