# CHANGELOG

## 2.9.0

- Adding option to normalize output of inverse_haversine [#78](https://github.com/mapado/haversine/pull/78) by [@thillerson](https://github.com/thillerson)
- add normalize_output to inverse_haversine_vector [#79](https://github.com/mapado/haversine/pull/79) by [@jdeniau](https://github.com/jdeniau)

## 2.8.1

- Use numpy kernel when using numba [#73](https://github.com/mapado/haversine/pull/73) by [@jdeniau](https://github.com/jdeniau)

## 2.8.0

- Performance improvements, especially with the `haversine_vector` function [#65](https://github.com/mapado/haversine/pull/65) by [jobh](https://github.com/jobh)

## 2.7.0

Official support of python 3.10, 3.11 and 3.12

## 2.6.0

- Check or normalize given lat/lon. [#49](https://github.com/mapado/haversine/issues/49) by [@uri-rodberg](https://github.com/uri-rodberg) and [@merschformann](https://github.com/merschformann)

## 2.5.1

- Reset type hinting for `inverse_haversine`

## 2.5.0

- [Minor break] Drop support for python 2.7 [#42](https://github.com/mapado/haversine/pull/42)

## 2.4.1

- Fix issue with python 2.7 compatibility. See [#41](https://github.com/mapado/haversine/issues/41)

## 2.4.0

- Added inver haversine functionality [#39](https://github.com/mapado/haversine/pull/39) by [@CrapsJeroen](https://github.com/CrapsJeroen)
- Adds radians and degrees units [#40](https://github.com/mapado/haversine/pull/40) by [@merschformann](https://github.com/merschformann)

## 2.3.1

- Fix license in setup.py [#38](https://github.com/mapado/haversine/pull/38) by [@kraj](https://github.com/kraj)

## 2.3.0

### Added

- Added the `comb` parameter for `haversine_vector` (thanks to [Fd-3741](https://github.com/Fd-3741)) [#34](https://github.com/mapado/haversine/pull/34)

## 2.2.0

### Added

- Added the `haversine_vector` function (thanks to [ccforgy](https://github.com/ccforgy)) [#26](https://github.com/mapado/haversine/pull/26)

### Changed

- Improve performance thanks to [adamchainz](https://github.com/adamchainz) [#27](https://github.com/mapado/haversine/pull/27)

## 2.1.2 - 2019-07-19

Fix typo in documentation

## 2.1.1 - 2019-05-07

Quick improvement left out at [#22](https://github.com/mapado/haversine/pull/22)
Renamed Units to Unit along the way, to comply with conventions (Breaking if you were on 2.1.0)

See more: [#23](https://github.com/mapado/haversine/pull/23) — Paolo Lammens

## 2.1.0 - 2019-05-07

General refactor: use Enum for available units, extract constants [#22](https://github.com/mapado/haversine/pull/22) — Paolo Lammens

## 2.0.0 - 2018-11-27

### Changed

- Add a `unit` parameter accepting different units (`miles`, `meter`, `feet`, etc.)
- [BREAKING] The `miles` and `nautical_miles` parameters have been removed and replaced by the `unit` parameter. See [#20](https://github.com/mapado/haversine/pull/20)

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

Du to a small change in the formula, the precision for miles aud nautical miles has slightly changed.
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
