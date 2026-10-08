import pytest

from haversine import Unit, haversine, haversine_path
from tests.geo_ressources import LYON, PARIS, NEW_YORK, LONDON


def test_path_is_sum_of_legs():
    route = [PARIS, LYON, NEW_YORK, LONDON]
    expected = sum(haversine(a, b) for a, b in zip(route, route[1:]))
    assert haversine_path(route) == pytest.approx(expected)


def test_two_points_equals_haversine():
    assert haversine_path([LYON, PARIS]) == pytest.approx(haversine(LYON, PARIS))


@pytest.mark.parametrize("points", [[], [PARIS]])
def test_fewer_than_two_points_is_zero(points):
    assert haversine_path(points) == 0.0


def test_units_and_string_units():
    route = [PARIS, LYON, LONDON]
    km = haversine_path(route)
    assert haversine_path(route, unit=Unit.METERS) == pytest.approx(km * 1000)
    assert haversine_path(route, unit="mi") == pytest.approx(haversine_path(route, unit=Unit.MILES))


def test_cumulative():
    route = [PARIS, LYON, LONDON]
    running = haversine_path(route, cumulative=True)
    assert len(running) == 3
    assert running[0] == 0.0
    assert running[1] == pytest.approx(haversine(PARIS, LYON))
    assert running[-1] == pytest.approx(haversine_path(route))
    assert haversine_path([], cumulative=True) == []
    assert haversine_path([PARIS], cumulative=True) == [0.0]


def test_accepts_generator():
    assert haversine_path(p for p in [PARIS, LYON]) == pytest.approx(haversine(PARIS, LYON))


def test_invalid_point_raises_unless_check_disabled():
    with pytest.raises(ValueError):
        haversine_path([PARIS, (91, 0)])
    haversine_path([PARIS, (91, 0)], check=False)


def test_normalize():
    assert haversine_path([PARIS, (PARIS[0], PARIS[1] + 360)], normalize=True) == pytest.approx(0.0, abs=1e-6)
