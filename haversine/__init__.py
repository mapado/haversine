from math import radians, cos, sin, asin, sqrt

AVG_EARTH_RADIUS = 6367.5  # in km


def haversine(point1, point2, miles=False):
    """ Calculate the great-circle distance bewteen two points on the Earth surface.

    Each point is defined by its latitide and longitude, in decimal degrees.

    Returns the distance bewteen the two points, by default in kilometers,
    or in miles if the ``miles`` parameter is set to True.

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
        return h * 0.6214  # in miles
    else:
        return h  # in kilometers
