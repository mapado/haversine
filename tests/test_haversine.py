from haversine import haversine, Unit

LYON = (45.7597, 4.8422)
PARIS = (48.8567, 2.3508)

EXPECTED = {Unit.KILOMETERS: 392.2172595594006,
            Unit.METERS: 392217.2595594006,
            Unit.MILES: 243.71250609539814,
            Unit.NAUTICAL_MILES: 211.78037755311516,
            Unit.FEET: 1286802.0326751503,
            Unit.INCHES: 15441624.392102592}


def haversine_test_factory(unit):
    def test():
        expected = EXPECTED[unit]
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

