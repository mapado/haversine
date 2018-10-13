# Haversine [![Build Status](https://travis-ci.org/mapado/haversine.svg?branch=master)](https://travis-ci.org/mapado/haversine)
Calculate the distance (in km or in miles) between two points on Earth,
located by their latitude and longitude.


## Example: distance between Lyon and Paris
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

## Installation
```bash
$ pip install haversine
```
## Contributing

Clone the project

Install [pipenv](https://github.com/pypa/pipenv).

Run `pipenv install`

Launch test with `pipenv run pytest`

