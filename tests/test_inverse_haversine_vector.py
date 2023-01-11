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
