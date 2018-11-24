from math import radians, cos, sin, asin, sqrt


def haversine(point1, point2, unit='km'):
    """ Calculate the great-circle distance between two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance between the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.

    """
    # mean earth radius - https://en.wikipedia.org/wiki/Earth_radius#Mean_radius
    AVG_EARTH_RADIUS_KM = 6371.0088

    # Units values taken from http://www.unitconversion.org/unit_converter/length.html
    conversions = {'km': 1,
                   'm': 1000,
                   'mi': 0.62137118693,
                   'nmi': 0.53995679617,
                   'ft': 3280.839895013,
                   'in': 39370.078740158}

    # get earth radius in required units
    avg_earth_radius = AVG_EARTH_RADIUS_KM * conversions[unit]

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
