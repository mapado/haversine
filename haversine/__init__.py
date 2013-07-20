from math import radians, cos, sin, asin, sqrt
from ctypes import cdll, c_float, c_int
from os.path import dirname, abspath, join

AVG_EARTH_RADIUS = 6371  # in km


def py_haversine(point1, point2, miles=False):
    """ Calculate the great-circle distance bewteen two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance bewteen the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.

    """
    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = list(map(radians, [lat1, lng1, lat2, lng2]))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(lng / 2) ** 2
    h = 2 * AVG_EARTH_RADIUS * asin(sqrt(d))
    if miles:
        return h * 0.621371  # in miles
    else:
        return h  # in kilometers


def c_haversine(point1, point2, miles=False):
    """
    Equivalent to the pure python haversine function, but calling
    a C function.
    """
    lat1, lng1 = point1
    lat2, lng2 = point2
    return so_haversine(lat1, lng1, lat2, lng2, int(miles))


# If the compiled shared object can be loaded, the haversine name
# will refer to the pure C implementation
# Otherwise, it will refer to the pure Python implementation
try:
    # The .so will automatically be compiled at install and will be placed
    # in the root of the virtualenv site packages directory
    # hence the relative path
    sopath = abspath(join(dirname(__file__), '..',  'libhsine.so'))
    dll = cdll.LoadLibrary(sopath)
    dll.haversine.restype = c_float
    dll.haversine.argtypes = [c_float, c_float, c_float, c_float, c_int]
    so_haversine = dll.haversine
    haversine = c_haversine
except OSError:  # fail to load shared object, fall back on pure python implementation
    haversine = py_haversine
