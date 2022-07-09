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
    p1, p2 = (0 - 180, -45 + 360), (0, 45)  # Use same values as below
    res = haversine_vector([p1], [p2], Unit.DEGREES, normalize=True)[0]
    assert res == 89.99999999999997


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
