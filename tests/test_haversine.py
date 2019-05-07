from haversine import haversine, Units

LYON = (45.7597, 4.8422)
PARIS = (48.8567, 2.3508)

EXPECTED = {Units.KILOMETERS: 392.2172595594006,
            Units.METERS: 392217.2595594006,
            Units.MILES: 243.71250609539814,
            Units.NAUTICAL_MILES: 211.78037755311516,
            Units.FEET: 1286802.0326751503,
            Units.INCHES: 15441624.392102592}


def haversine_test_factory(unit):
    def test():
        expected = EXPECTED[unit]
        assert haversine(LYON, PARIS, unit=unit) == expected
        assert isinstance(unit.value, str)
        assert haversine(LYON, PARIS, unit=unit.value) == expected

    return test


test_kilometers = haversine_test_factory(Units.KILOMETERS)
test_meters = haversine_test_factory(Units.METERS)
test_miles = haversine_test_factory(Units.MILES)
test_nautical_miles = haversine_test_factory(Units.NAUTICAL_MILES)
test_feet = haversine_test_factory(Units.FEET)
test_inches = haversine_test_factory(Units.INCHES)


def test_units_enum():
    from haversine.haversine import _CONVERSIONS
    assert all(unit in _CONVERSIONS for unit in Units)

