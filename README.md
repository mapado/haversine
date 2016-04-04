# Haversine [![Build Status](https://travis-ci.org/mapado/haversine.svg?branch=master)](https://travis-ci.org/mapado/haversine)
Calculate the distance (in km or in miles) between two points on Earth,
located by their latitude and longitude.


## Example: distance between Lyon and Paris
```python
>>> from haversine import haversine
>>> lyon = (45.7597, 4.8422)
>>> paris = (48.8567, 2.3508)
>>> haversine(lyon, paris)
392.21671780659625  # in kilometers
>>> haversine(lyon, paris, miles=True)
243.71209416020253  # in miles
```

## Installation
```bash
$ pip install haversine
```
