# Haversine [![Build Status](https://travis-ci.org/marmig0404/haversine.svg?branch=patch-1)](https://travis-ci.com/marmig0404/haversine)
## Haversine Formula
Calculate the distance (in km or in miles) between two points on Earth,
located by their latitude and longitude.


### Example: distance between Lyon and Paris
```python
from haversine import haversine

lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

haversine(lyon, paris)
# 392.2172595594006  # in kilometers

haversine(lyon, paris, miles=True)
# 243.7125041070121  # in miles

haversine(lyon, paris, nautical_miles=True)
# 211.7803748731092  # in nautical miles
```
## Inverse Haversine Formula
Calculates a point from a given vector (distance and direction) and start point.
Currently only supports cardinal directions (north, east, south, west).

## Example: Finding arbitary point from Paris
```python
from haversine import inverse_haversine

paris = (48.8567, 2.3508) # (lat, lon)

# Finding 32 km west of Paris
inverse_haversine(paris, 32, 'west')
# returns tuple (48.8567, 1.91340)

# Finding 50 miles north of Paris
inverse_haversine(paris, 50, 'north', miles=True)
# returns tuple (49.48035, 2.3508)

# Finding 10 nautical miles south of Paris
inverse_haversine(paris, 10, 'south', nautical_miles=True)
# returns tuple (48.69014, 2.3508)
```

## Installation
```bash
$ pip install haversine
```
## Contributing

Clone the project

Install [pipenv](https://github.com/pypa/pipenv).

Run `pipenv install`

Launch test with `pipenv run pytest`

