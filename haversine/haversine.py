from math import radians, cos, sin, asin, sqrt
from enum import Enum


# mean earth radius - https://en.wikipedia.org/wiki/Earth_radius#Mean_radius
_AVG_EARTH_RADIUS_KM = 6371.0088


class Unit(Enum):
    """
    Enumeration of supported units.
    The full list can be checked by iterating over the class; e.g.
    the expression `tuple(Unit)`.
    """

    KILOMETERS = 'km'
    METERS = 'm'
    MILES = 'mi'
    NAUTICAL_MILES = 'nmi'
    FEET = 'ft'
    INCHES = 'in'


# Unit values taken from http://www.unitconversion.org/unit_converter/length.html
_CONVERSIONS = {Unit.KILOMETERS:       1.0,
                Unit.METERS:           1000.0,
                Unit.MILES:            0.621371192,
                Unit.NAUTICAL_MILES:   0.539956803,
                Unit.FEET:             3280.839895013,
                Unit.INCHES:           39370.078740158}

def get_avg_earth_radius(unit):
    unit = Unit(unit)
    return _AVG_EARTH_RADIUS_KM * _CONVERSIONS[unit]

def haversine(point1, point2, unit=Unit.KILOMETERS):
    """ Calculate the great-circle distance between two points on the Earth surface.

    Takes two 2-tuples, containing the latitude and longitude of each point in decimal degrees,
    and, optionally, a unit of length.

    :param point1: first point; tuple of (latitude, longitude) in decimal degrees
    :param point2: second point; tuple of (latitude, longitude) in decimal degrees
    :param unit: a member of haversine.Unit, or, equivalently, a string containing the
                 initials of its corresponding unit of measurement (i.e. miles = mi)
                 default 'km' (kilometers).

    Example: ``haversine((45.7597, 4.8422), (48.8567, 2.3508), unit=Unit.METERS)``

    Precondition: ``unit`` is a supported unit (supported units are listed in the `Unit` enum)

    :return: the distance between the two points in the requested unit, as a float.

    The default returned unit is kilometers. The default unit can be changed by
    setting the unit parameter to a member of ``haversine.Unit``
    (e.g. ``haversine.Unit.INCHES``), or, equivalently, to a string containing the
    corresponding abbreviation (e.g. 'in'). All available units can be found in the ``Unit`` enum.
    """

    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1 = radians(lat1)
    lng1 = radians(lng1)
    lat2 = radians(lat2)
    lng2 = radians(lng2)

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2

    return 2 * get_avg_earth_radius(unit) * asin(sqrt(d))


def haversine_vector(array1, array2, unit=Unit.KILOMETERS, comb=False):
    '''
    The exact same function as "haversine", except that this
    version replaces math functions with numpy functions.
    This may make it slightly slower for computing the haversine
    distance between two points, but is much faster for computing
    the distance between two vectors of points due to vectorization.
    '''
    try:
        import numpy
    except ModuleNotFoundError:
        return 'Error, unable to import Numpy,\
        consider using haversine instead of haversine_vector.'

    # ensure arrays are numpy ndarrays
    if not isinstance(array1, numpy.ndarray):
        array1 = numpy.array(array1)
    if not isinstance(array2, numpy.ndarray):
        array2 = numpy.array(array2)

    # ensure will be able to iterate over rows by adding dimension if needed
    if array1.ndim == 1:
        array1 = numpy.expand_dims(array1, 0)
    if array2.ndim == 1:
        array2 = numpy.expand_dims(array2, 0)

    # Asserts that both arrays have same dimensions if not in combination mode
    if not comb:
        if array1.shape != array2.shape:
            raise IndexError("When not in combination mode, arrays must be of same size. If mode is required, use comb=True as argument.")

    # unpack latitude/longitude
    lat1, lng1 = array1[:, 0], array1[:, 1]
    lat2, lng2 = array2[:, 0], array2[:, 1]

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1 = numpy.radians(lat1)
    lng1 = numpy.radians(lng1)
    lat2 = numpy.radians(lat2)
    lng2 = numpy.radians(lng2)

    # If in combination mode, turn coordinates of array1 into column vectors for broadcasting
    if comb:
        lat1 = numpy.expand_dims(lat1,axis=0)
        lng1 = numpy.expand_dims(lng1,axis=0)
        lat2 = numpy.expand_dims(lat2,axis=1)
        lng2 = numpy.expand_dims(lng2,axis=1)
    
    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = (numpy.sin(lat * 0.5) ** 2
         + numpy.cos(lat1) * numpy.cos(lat2) * numpy.sin(lng * 0.5) ** 2)

    return 2 * get_avg_earth_radius(unit) * numpy.arcsin(numpy.sqrt(d))
