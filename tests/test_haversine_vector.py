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
        assert haversine_vector(
            LYON, PARIS, unit=unit.value) == expected_lyon_paris

    return test_lyon_paris(unit)


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
        haversine_vector([oob_from], [oob_to], Unit.DEGREES, normalize=True),
        haversine_vector([proper_from], [proper_to],
                         Unit.DEGREES, normalize=True),
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
        haversine_vector([oob_from], [oob_to])
    with pytest.raises(ValueError):
        haversine_vector([oob_from], [oob_to], normalize=False)


def test_haversine_vector_comb():
    unit = Unit.KILOMETERS
    expected = [
        [EXPECTED_LYON_PARIS[unit],  EXPECTED_LONDON_PARIS[unit]],
        [EXPECTED_LYON_NEW_YORK[unit], EXPECTED_LONDON_NEW_YORK[unit]]
    ]

    assert_allclose(  # See https://numpy.org/doc/stable/reference/generated/numpy.testing.assert_allclose.html#numpy.testing.assert_allclose
        haversine_vector([LYON, LONDON], [PARIS, NEW_YORK], unit, comb=True),
        expected
    )


def test_units_enum():
    from haversine.haversine import _CONVERSIONS
    assert all(unit in _CONVERSIONS for unit in Unit)
