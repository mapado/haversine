from math import degrees, radians, cos, sin, acos, asin, sqrt

# mean earth radius - https://en.wikipedia.org/wiki/Earth_radius#Mean_radius
AVG_EARTH_RADIUS_KM = 6371.0088
AVG_EARTH_RADIUS_MI = 3958.7613
AVG_EARTH_RADIUS_NMI = 3440.0695

def haversine(point1, point2, miles=False, nautical_miles=False):
    """ Calculate the great-circle distance between two points on the Earth surface.

    :input: two 2-tuples, containing the latitude and longitude of each point
    in decimal degrees.

    Example: haversine((45.7597, 4.8422), (48.8567, 2.3508))

    :output: Returns the distance between the two points.
    The default unit is kilometers. Miles can be returned
    if the ``miles`` parameter is set to True.

    """
    # get earth radius in required units
    if miles:
        avg_earth_radius = AVG_EARTH_RADIUS_MI
    elif nautical_miles:
        avg_earth_radius = AVG_EARTH_RADIUS_NMI
    else:
        avg_earth_radius = AVG_EARTH_RADIUS_KM

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


def inverse_haversine(point, distance, direction, miles=False, nautical_miles=False):

    if miles:
        avg_earth_radius = AVG_EARTH_RADIUS_MI
    elif nautical_miles:
        avg_earth_radius = AVG_EARTH_RADIUS_NMI
    else:
        avg_earth_radius = AVG_EARTH_RADIUS_KM

    lat1, lng1 = point
    lat1, lng1 = map(radians, (lat1, lng1))
    d = sin(distance / (2 * avg_earth_radius)) ** 2

    if direction == "north":
        return_lng = lng1
        delta = acos((1 - 2 * d) / cos(return_lng - lng1))
        return_lat = lat1 + delta

    elif direction == "east":
        return_lat = lat1
        delta = 2 * asin(sqrt(d)/cos(return_lat))
        return_lng = lng1 + delta

    elif direction == "south":
        return_lng = lng1
        delta = acos((1 - 2 * d) / cos(return_lng - lng1))
        return_lat = lat1 - delta

    elif direction == "west":
        return_lat = lat1
        delta = 2 * asin(sqrt(d)/cos(return_lat))
        return_lng = lng1 - delta

    return_lat, return_lng = map(degrees, (return_lat, return_lng))
    return return_lat, return_lng
