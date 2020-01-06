from haversine import haversine_vector, Unit

LYON = (45.7597, 4.8422)
PARIS = (48.8567, 2.3508)
NEW_YORK = (40.7033962, -74.2351462)

EXPECTED_LYON_PARIS = {Unit.KILOMETERS: 392.2172595594006,
            Unit.METERS: 392217.2595594006,
            Unit.MILES: 243.71250609539814,
            Unit.NAUTICAL_MILES: 211.78037755311516,
            Unit.FEET: 1286802.0326751503,
            Unit.INCHES: 15441624.392102592}
EXPECTED_LYON_NEW_YORK = {Unit.KILOMETERS: 6163.43638211,
            Unit.METERS: 61634363.8211 }
EXPECTED_PARIS_NEW_YORK = {Unit.KILOMETERS: 5853.32898662,
            Unit.METERS: 58533289.8662 }


def haversine_test_factory(unit):
    def test():
        expected_lyon_paris = EXPECTED_LYON_PARIS[unit]
        expected_lyon_new_york = EXPECTED_LYON_NEW_YORK[unit]
        expected_paris_new_york = EXPECTED_PARIS_NEW_YORK[unit]

        assert haversine_vector(LYON, PARIS, unit=unit) == expected_lyon_paris
        assert isinstance(unit.value, str)
        assert haversine_vector(LYON, PARIS, unit=unit.value) == expected_lyon_paris

    return test


test_kilometers = haversine_test_factory(Unit.KILOMETERS)
test_meters = haversine_test_factory(Unit.METERS)


def test_units_enum():
    from haversine.haversine import _CONVERSIONS
    assert all(unit in _CONVERSIONS for unit in Unit)


