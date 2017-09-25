Atmosfera Estandar Library
================================

This is a library with the internation standard atmosphere model (ISA) and the correponding method 
to calculate atmospheric parameters at different attitudes, or getting the attitude for a given set
of pressure and temperature.

Examples of code:

Using altura as input

```python
In [5]: import atmosfera_estandar.atmosfera_estandar as at

In [7]: h, _, p, t, rho, mu, vson = at.atmosfera_estandar('altura', 1500, deltaT=0)

In [9]: print("altura: {} m ".format(h))
altura: 1500 m

In [10]: print("presion: {} Pa ".format(p))
presion: 84547.39056761812 Pa

In [11]: print("temperatura: {} K ".format(t))
temperatura: 278.37954545454545 K

In [12]: print("densidad: {} km/m**3 ".format(rho))
densidad: 1.058232243881217 km/m**3

In [14]: print("viscocidad: {} km/m/s ".format(mu))
viscocidad: 1.7418473749959833e-05 km/m/s

In [15]: print("velocidad del sonido: {} m/s ".format(vson))
velocidad del sonido: 334.4441677823615 m/s
```

Using presion as input

```python
In [16]: h, _, p, t, rho, mu, vson = at.atmosfera_estandar('presion', 65000.0, deltaT=10)

In [17]: print("altura: {} m ".format(h))
altura: 3588.5630187333736 m

In [18]: print("presion: {} Pa ".format(p))
presion: 65000.0 Pa

In [19]: print("temperatura: {} K ".format(t))
temperatura: 274.7754054279776 K

In [20]: print("densidad: {} km/m**3 ".format(rho))
densidad: 0.8242398401129738 km/m**3

In [21]: print("viscocidad: {} km/m/s ".format(mu))
viscocidad: 1.7241131394354893e-05 km/m/s

In [22]: print("velocidad del sonido: {} m/s ".format(vson))
velocidad del sonido: 332.27211423916 m/s
```

There is also a GUI asociate with this library. It uses pyside and Qt. It consist of a simple dialog box containing the input parameters and results of the atmosfera_estandar method. GUI knows how to display results in imperial units, but behind all calculations are implemented in Iternational Units.

