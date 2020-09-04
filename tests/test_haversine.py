from haversine import haversine, haversine_vector, Unit
from numpy.testing import assert_allclose

LYON = (45.7597, 4.8422)
PARIS = (48.8567, 2.3508)
LONDON = (51.509865, -0.118092)
NEW_YORK = (40.7033962, -74.2351462)

EXPECTED_LYON_PARIS = {Unit.KILOMETERS: 392.2172595594006,
            Unit.METERS: 392217.2595594006,
            Unit.MILES: 243.71250609539814,
            Unit.NAUTICAL_MILES: 211.78037755311516,
            Unit.FEET: 1286802.0326751503,
            Unit.INCHES: 15441624.392102592}


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


def test_units_enum():
    from haversine.haversine import _CONVERSIONS
    assert all(unit in _CONVERSIONS for unit in Unit)


def test_haversine_vector_comb():
    expected = [[ 392.21725956,  343.37455271], [6163.43638211, 5586.48447423]]

    assert_allclose( # See https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose
        haversine_vector([LYON, LONDON], [PARIS, NEW_YORK], Unit.KILOMETERS, comb=True),
        expected
    )