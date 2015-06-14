#define _USE_MATH_DEFINES
#include <math.h>
#include <stdio.h>

const float EARTH_RADIUS = 6371.0;


float deg_to_rad(float deg)
{
  return (deg * M_PI) / 180.0;
}

float haversine(float lat1, float lng1, float lat2, float lng2, int miles)
{
  float dlat, dlng, a, d;

  // convert all decimal arguments to radiants
  lat1 = deg_to_rad(lat1);
  lng1 = deg_to_rad(lng1);
  lat2 = deg_to_rad(lat2);
  lng2 = deg_to_rad(lng2);

  // compute haversine
  dlat = lat2 - lat1;
  dlng = lng2 - lng1;
  a = sin(pow((dlat/2), 2) + cos(lat1)*cos(lat2)*pow(sin(dlng/2),2));
  d = 2 * EARTH_RADIUS * asin(sqrt(a));
  if (miles == 1){
    return d * 0.621371;  // distance expressed in miles
  }
  else {
    return d;  // distance expressed in kilometers
  }
}
