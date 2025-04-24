# Haversine

Calculate the distance (in various units) between two points on Earth using their latitude and longitude.

## Installation

```sh
pip install haversine
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
>> 243.71250609539814  # in miles

# you can also use the string abbreviation for units:
haversine(lyon, paris, unit='mi')
>> 243.71250609539814  # in miles

haversine(lyon, paris, unit=Unit.NAUTICAL_MILES)
>> 211.78037755311516  # in nautical miles
```

The lat/lon values need to be provided in degrees of the ranges [-90,90] (lat) and [-180,180] (lon).
If values are outside their ranges, an error will be raised. This can be avoided by automatic normalization via the `normalize` parameter.

The `haversine.Unit` enum contains all supported units:

```python
import haversine

print(tuple(haversine.Unit))
```

outputs

```text
(<Unit.KILOMETERS: 'km'>, <Unit.METERS: 'm'>, <Unit.MILES: 'mi'>,
 <Unit.NAUTICAL_MILES: 'nmi'>, <Unit.FEET: 'ft'>, <Unit.INCHES: 'in'>,
 <Unit.RADIANS: 'rad'>, <Unit.DEGREES: 'deg'>)
```

#### Note for radians and degrees

The radian and degrees returns the [great circle distance](https://en.wikipedia.org/wiki/Great-circle_distance) between two points on a sphere.

Notes:

- on a unit-sphere the angular distance in radians equals the distance between the two points on the sphere (definition of radians)
- When using "degree", this angle is just converted from radians to degrees

### Inverse Haversine Formula

Calculates a point from a given vector (distance and direction) and start point.
Currently explicitly supports both cardinal (north, east, south, west) and intercardinal (northeast, southeast, southwest, northwest) directions.
But also allows for explicit angles expressed in Radians.

## Example: Finding arbitrary point from Paris

```python
from haversine import inverse_haversine, Direction
from math import pi
paris = (48.8567, 2.3508) # (lat, lon)
# Finding 32 km west of Paris
inverse_haversine(paris, 32, Direction.WEST)
# returns tuple (48.85587279023947, 1.9134085092836945)
# Finding 32 km southwest of Paris
inverse_haversine(paris, 32, pi * 1.25)
# returns tuple (48.65279552300661, 2.0427666779658806)
# Finding 50 miles north of Paris
inverse_haversine(paris, 50, Direction.NORTH, unit=Unit.MILES)
# returns tuple (49.58035791599536, 2.3508)
# Finding 10 nautical miles south of Paris
inverse_haversine(paris, 10, Direction.SOUTH, unit=Unit.NAUTICAL_MILES)
# returns tuple (48.690145868497645, 2.3508)
```

### Performance optimisation for distances between all points in two vectors

You will need to install [numpy](https://pypi.org/project/numpy/) in order to gain performance with vectors.
For optimal performance, you can turn off coordinate checking by adding `check=False` and install the optional packages [numba](https://pypi.org/project/numba/) and [icc_rt](https://pypi.org/project/icc_rt/).

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
