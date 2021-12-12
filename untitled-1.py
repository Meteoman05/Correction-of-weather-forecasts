import numpy as np
from metpy.units import units
import metpy.calc

lat = np.linspace(55.7, 55.8, 3)
lon = np.linspace(37.6, 37.7, 3)
dx, dy = metpy.calc.lat_lon_grid_deltas(lat, lon)

a, b, c = 273, -5, 8

pottemp = np.array([[a, a, a],
                    [a, a, a],
                    [a, a, a]]) * units.kelvin

u = np.array([[b, b, b],
              [b, b, b],
              [b, b, b]]) * units('m/s')

v = np.array([[c, c, c],
              [c, c, c],
              [c, c, c]]) * units('m/s')

print(metpy.calc.frontogenesis(pottemp, u, v, dx=dx, dy=dy))
