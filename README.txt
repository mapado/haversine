Haversine
---------

Calculate the distance (in km or in miles) bewteen two points on Earth,
located by their latitude and longitude.


Example: distance bewteen Lyon and Paris

>>> from haversine import haversine
>>> lyon = (45.7597, 4.8422)
>>> paris = (48.8567, 2.3508)
>>> haversine(lyon, paris)
392.00124794121825  # in kilometers
>>> haversine(lyon, paris, miles=True)
243.589575470673  # in miles
