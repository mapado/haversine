from .  import haversine_baseline as baseline
import haversine as current
import numpy as np
import pytest
from timeit import timeit

def assert_performance(func, number):
    # Interleave measurements and compare fastest current to median baseline.
    # All in an attempt to avoid spurious errors caused by fluctuating load on
    # the runner.
    t_baseline, t_current = [], []
    for repeat in range(5):
        t_baseline.append(timeit(lambda: func(baseline),  number=number))
        t_current.append(timeit(lambda: func(current),  number=number))

    perf_ratio = np.min(t_current) / np.median(t_baseline)
    assert perf_ratio <= 1.1


@pytest.mark.parametrize(
    "check", [False, True]
)
@pytest.mark.parametrize(
    "normalize", [False, True]
)
def test_haversine(check, normalize):
    if check == normalize == True:
        pytest.skip()
    assert_performance(lambda m: m.haversine((0,1), (2,3), check=check, normalize=normalize),
                       number=100000)


@pytest.mark.parametrize(
    "check", [False, True]
)
@pytest.mark.parametrize(
    "normalize", [False, True]
)
def test_haversine_vector(check, normalize):
    if check == normalize == True:
        pytest.skip()
    arr = np.random.uniform(size=(1000, 2))
    assert_performance(lambda m: m.haversine_vector(arr, arr, check=check, normalize=normalize),
                       number=1000)


def test_inverse_haversine():
    assert_performance(lambda m: m.inverse_haversine((0,1), 2, 3),
                       number=100000)


def test_inverse_haversine_vector():
    arr = np.random.uniform(size=(1000, 2))
    assert_performance(lambda m: m.inverse_haversine_vector(arr, *arr.T),
                       number=1000)
