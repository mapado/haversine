# Haversine [![Build Status](https://travis-ci.org/mapado/haversine.svg?branch=master)](https://travis-ci.org/mapado/haversine)

Calculate the distance (in various units) between two points on Earth using their latitude and longitude.


## Example

### Calculate the distance between Lyon and Paris

```python
from haversine import haversine, Unit

lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)

haversine(lyon, paris)
>> 392.2172595594006  # in kilometers

haversine(lyon, paris, unit=Unit.MILES)
>> 243.71201856934454  # in miles

# you can also use the string abbreviation for units:
haversine(lyon, paris, unit='mi')
>> 243.71201856934454  # in miles

haversine(lyon, paris, unit=Unit.NAUTICAL_MILES)
>> 211.78037755311516  # in nautical miles
```

The `haversine.Unit` enum contains all supported units:

```python
import haversine

print(tuple(haversine.Unit))
```

outputs

```text
(<Unit.FEET: 'ft'>, <Unit.INCHES: 'in'>, <Unit.KILOMETERS: 'km'>, 
 <Unit.METERS: 'm'>, <Unit.MILES: 'mi'>, <Unit.NAUTICAL_MILES: 'nmi'>)
```

## Installation

```bash
$ pip install haversine
```
## Contributing

Clone the project.

Install [pipenv](https://github.com/pypa/pipenv).

Run `pipenv install --dev`

Launch test with `pipenv run pytest`
