# Haversine [![Build Status](https://travis-ci.org/mapado/haversine.svg?branch=master)](https://travis-ci.org/mapado/haversine)

Calculate the distance (in various units) between two points on Earth using their latitude and longitude.

## Installation

```bash
$ pip install haversine
```

## Usage

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

### Performance optimisation for distances between all points in two vectors

You will need to add [numpy](https://pypi.org/project/numpy/) in order to gain performance with vectors.

You can then do this:

```python
from haversine import haversine_vector, Unit

lyon = (45.7597, 4.8422) # (lat, lon)
paris = (48.8567, 2.3508)
new_york = (40.7033962, -74.2351462)

haversine_vector([lyon, lyon], [paris, new_york], Unit.KILOMETERS)

>> array([ 392.21725956, 6163.43638211])
```

It is generally slower to use `haversine_vector` to get distance between two points, but can be really fast to compare distances between two vectors.

### Combine matrix

You can generate a matrix of all combinations between coordinates in different vectors by setting `comb` parameter as True.

```python
from haversine import haversine_vector, Unit

lyon = (45.7597, 4.8422) # (lat, lon)
london = (51.509865, -0.118092)
paris = (48.8567, 2.3508)
new_york = (40.7033962, -74.2351462)

haversine_vector([lyon, london], [paris, new_york], Unit.KILOMETERS, comb=True)

>> array([[ 392.21725956,  343.37455271],
 	  [6163.43638211, 5586.48447423]])
```

The output array from the example above returns the following table:

|        |       Paris       |       New York       |
| ------ | :---------------: | :------------------: |
| Lyon   |  Lyon <\-> Paris  |  Lyon <\-> New York  |
| London | London <\-> Paris | London <\-> New York |

By definition, if you have a vector _a_ with _n_ elements, and a vector _b_ with _m_ elements. The result matrix _M_ would be $n x m$ and a element M\[i,j\] from the matrix would be the distance between the ith coordinate from vector _a_ and jth coordinate with vector _b_.

## Contributing

Clone the project.

Install [pipenv](https://github.com/pypa/pipenv).

Run `pipenv install --dev`

Launch test with `pipenv run pytest`
