from haversine import haversine_vector, Unit
from numpy.testing import assert_allclose

from tests.geo_ressources import EXPECTED_LONDON_PARIS, EXPECTED_LYON_NEW_YORK, EXPECTED_LYON_PARIS, EXPECTED_LONDON_NEW_YORK, LYON, PARIS, NEW_YORK, LONDON

def test_pair(unit):
    def test_lyon_paris(unit):
        expected_lyon_paris = EXPECTED_LYON_PARIS[unit]
        assert haversine_vector(LYON, PARIS, unit=unit) == expected_lyon_paris
        assert isinstance(unit.value, str)
        assert haversine_vector(LYON, PARIS, unit=unit.value) == expected_lyon_paris

    return test_lyon_paris(unit)


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

test_pair(Unit.KILOMETERS)
test_pair(Unit.METERS)
test_pair(Unit.INCHES)
test_haversine_vector_comb()

def test_units_enum():
    from haversine.haversine import _CONVERSIONS
    assert all(unit in _CONVERSIONS for unit in Unit)

test_units_enum()