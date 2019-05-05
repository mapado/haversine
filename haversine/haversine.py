from math import radians, cos, sin, asin, sqrt
from enum import Enum


# mean earth radius - https://en.wikipedia.org/wiki/Earth_radius#Mean_radius
_AVG_EARTH_RADIUS_KM = 6371.0088


class Units(Enum):
    """
    Enumeration of supported units.
    The full list can be checked by iterating over the class; e.g.
    the expression `tuple(Units)`.
    """

    KILOMETERS = 'km'
    METERS = 'm'
    MILES = 'mi'
    NAUTICAL_MILES = 'nmi'
    FEET = 'ft'
    INCHES = 'in'


# Units values taken from http://www.unitconversion.org/unit_converter/length.html
_CONVERSIONS = {Units.KILOMETERS.value:       1.0,
                Units.METERS.value:           1000.0,
                Units.MILES.value:            0.621371192,
                Units.NAUTICAL_MILES.value:   0.539956803,
                Units.FEET.value:             3280.839895013,
                Units.INCHES.value:           39370.078740158}


def haversine(point1, point2, unit=Units.KILOMETERS):
    """ Calculate the great-circle distance between two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Keyword arguments:
    unit -- a string containing the initials of a unit of measurement (i.e. miles = mi)
            default 'km' (kilometers).

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance between the two points.

    The default returned unit is kilometers. The default unit can be changed by
    setting the unit parameter to a string containing the initials of the desired unit.
    Other available units are miles (mi), nautic miles (nmi), meters (m),
    feets (ft) and inches (in).

    """

    # get earth radius in required units
    unit = unit.value if isinstance(unit, Units) else unit
    avg_earth_radius = _AVG_EARTH_RADIUS_KM * _CONVERSIONS[unit]

    # unpack latitude/longitude
    lat1, lng1 = point1
    lat2, lng2 = point2

    # convert all latitudes/longitudes from decimal degrees to radians
    lat1, lng1, lat2, lng2 = map(radians, (lat1, lng1, lat2, lng2))

    # calculate haversine
    lat = lat2 - lat1
    lng = lng2 - lng1
    d = sin(lat * 0.5) ** 2 + cos(lat1) * cos(lat2) * sin(lng * 0.5) ** 2

    return 2 * avg_earth_radius * asin(sqrt(d))
