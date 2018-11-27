# Haversine [![Build Status](https://travis-ci.org/mapado/haversine.svg?branch=master)](https://travis-ci.org/mapado/haversine)

Calculate the distance (in km or in miles) between two points on Earth using their latitude and longitude.


## Example

### Calculate the distance between Lyon and Paris

```python
from haversine import haversine

lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

haversine(lyon, paris)
>> 392.2172595594006  # in kilometers

haversine(lyon, paris, unit='mi')
>> 243.71201856934454  # in miles

haversine(lyon, paris, unit='nmi')
>> 211.78037755311516  # in nautical miles
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
