from haversine import inverse_haversine_vector, Unit, Direction
from numpy import isclose
from math import pi
import pytest

from tests.geo_ressources import LYON, PARIS, NEW_YORK, LONDON


@pytest.mark.parametrize(
    "point, dir, dist, result",
    [
        (PARIS, Direction.NORTH, 32, (49.144444, 2.3508)),
        (PARIS, 0, 32, (49.144444, 2.3508)),
        (LONDON, Direction.WEST, 50, (51.507778, -0.840556)),
        (LONDON, pi * 1.5, 50, (51.507778, -0.840556)),
        (NEW_YORK, Direction.SOUTH, 15, (40.568611, -74.235278)),
        (NEW_YORK, Direction.NORTHWEST, 50, (41.020556, -74.656667)),
        (NEW_YORK, pi * 1.25, 50, (40.384722, -74.6525)),
    ],
)
def test_inverse_kilometers(point, dir, dist, result):
    assert isclose(inverse_haversine_vector([point], [dist], [dir]),
                   ([result[0]], [result[1]]), rtol=1e-5).all()

def test_inverse_normalization():
    twoDegreesAtEquator = 222390.1
    point = (0.0, -179.0)

    # non-breaking behavior without normalization
    result = inverse_haversine_vector(
        [point, LONDON], [twoDegreesAtEquator, 50], [Direction.WEST, Direction.WEST], Unit.METERS)

    # assert result is a Tuple
    assert isinstance(result, tuple)

    # assert result is a Tuple of array
    latArray, lngArray = result

    assert isclose(lngArray[0], -181.0, rtol=1e-5,)

    # behavior with normalization
    result = inverse_haversine_vector(
        [point, LONDON], [twoDegreesAtEquator, 50000], direction=[Direction.WEST, Direction.WEST],
        unit=Unit.METERS, normalize_output=True,)

    
    # assert result is a Tuple
    assert isinstance(result, tuple)

    # assert result is a Tuple of array
    latArray, lngArray = result

    assert isclose(lngArray[0], 179.0, rtol=1e-5,).all()
    assert isclose(lngArray[1], -0.840556, rtol=1e-5,).all()