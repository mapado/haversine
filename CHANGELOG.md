# CHANGELOG

## 2.1.0 - 2019-05-07

General refactor: use Enum for available units, extract constants [#22](https://github.com/mapado/haversine/pull/22) — Paolo Lammens

## 2.0.0 - 2018-11-27

### Changed

* Add a `unit` parameter accepting different units (`miles`, `meter`, `feet`, etc.)
* [BREAKING] The `miles` and  `nautical_miles` parameters have been removed and replaced by the `unit` parameter. See [#20](https://github.com/mapado/haversine/pull/20)

### How to upgrade

If you did not use the `miles` or `nautical_miles`, you are good to go, this is non-breaking for you !

If you did use `miles` or `nautical_miles`, you just need to do that: 

```diff
- haversine(lyon, paris, miles=True)
+ haversine(lyon, paris, unit='mi')
```

```diff
- haversine(lyon, paris, nautical_miles=True)
+ haversine(lyon, paris, unit='nmi')
```

Du to a small change in the formula, the precision for miles aud nautical miles has slighty changed. 
Example : distance between Lyon, France and Paris, France changed from `243.7125041070121 miles` to `243.71250609539814 miles`. Same for nautical miles.


## 1.0.2 - 2018-10-13

slightly better precision [#17](https://github.com/mapado/haversine/pull/17)

## 1.0.1 - 2018-10-10

fix wrong definition in setup.py

## 1.0.0 - 2018-10-10

No changes, haversine package has been stable and functional for years now. Time to make a 1.0 version :)

(in fact there is one breaking changes but it concern the 0.5.0 version published just 10 minutes before 1.0 ;). In that case `nmiles` has been changed to `nautical_miles` for readability)

## 0.5.0 - 2018-10-10

Add nautical miles support

## 0.4.6

Fixed typos in README and docstring

## 0.4.5

Fixed issue with int instead of float [#6](https://github.com/mapado/haversine/pull/6/files)

## 0.4.3 - 0.4.4

- Remove useless code [#5](https://github.com/mapado/haversine/pull/5)

## 0.4.2

- Remove cPython usage: fail on Windows, no real perf gain [5d0ff179](https://github.com/mapado/haversine/commit/5d0ff179741b8417965d94dcb21f39ddbce674f8)
