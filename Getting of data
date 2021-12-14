from datetime import datetime, date, time
import pandas as pd
import xarray as xr
import numpy as np
import matplotlib.pyplot as plt

# from metpy.units import units
# import metpy.calc

date1 = datetime.now().strftime('%Y%m%d')
date2 = datetime.fromtimestamp((datetime.timestamp(datetime.now()) - 86400)).strftime('%Y%m%d')


# lat = np.linspace(55.7, 55.8, 3)
# lon = np.linspace(37.6, 37.7, 3)
# dx, dy = metpy.calc.lat_lon_grid_deltas(lat, lon)


gfs1 = xr.open_dataset('https://nomads.ncep.noaa.gov/dods/gfs_0p25/gfs'+date1+'/gfs_0p25_00z')
gfs = gfs1.sel(lon=37.5, lat=55.75, method='nearest')
gfs = gfs[['prmslmsl', 'tmpprs']]
gfs = gfs.sel(time=gfs.time[0:24], lev=850)
meteo1 = gfs.to_dataframe()

gfs1 = xr.open_dataset('https://nomads.ncep.noaa.gov/dods/gfs_0p25/gfs'+date2+'/gfs_0p25_18z')
gfs = gfs1.sel(lon=37.5, lat=55.75, method='nearest')
gfs = gfs[['prmslmsl', 'tmpprs']]
gfs = gfs.sel(time=gfs.time[0:24], lev=850)
meteo2 = gfs.to_dataframe()
meteo2 = meteo2[0:2]

meteo1 = meteo1.drop(['lat', 'lon', 'lev'], axis = 'columns')
meteo2 = meteo2.drop(['lat', 'lon', 'lev'], axis = 'columns')

meteo = meteo2.append(meteo1)

pmsl = []
tmp = []
prs_tend = [0]
tmp_adv = [0]
prs_tend_delta = [0, 0]
tmp_adv_delta = [0, 0]
for i in range(len(meteo)):
    j = meteo.iloc[i, 0]/100
    j = round(j, 2)
    pmsl.append(j)
meteo['prmslmsl'] = pmsl
    
for i in range(len(meteo)):
    j = meteo.iloc[i, 1] - 273.15
    j = round(j, 2)
    tmp.append(j)
meteo['tmpprs'] = tmp

for i in range(1, len(meteo)):
    j = meteo.iloc[i, 0] - meteo.iloc[i-1, 0]
    prs_tend.append(j)
meteo['prs_tend'] = prs_tend

for i in range(1, len(meteo)):
    j = meteo.iloc[i, 1] - meteo.iloc[i-1, 1]
    tmp_adv.append(j)
meteo['tmp_adv'] = tmp_adv

for i in range(2, len(meteo)):
    j = meteo.iloc[i, 2] - meteo.iloc[i-1, 2]
    prs_tend_delta.append(j)
meteo['prs_tend_delta'] = prs_tend_delta

for i in range(2, len(meteo)):
    j = meteo.iloc[i, 3] - meteo.iloc[i-1, 3]
    tmp_adv_delta.append(j)
meteo['tmp_adv_delta'] = tmp_adv_delta





# meteo['tmp2m'] = round((meteo['tmp2m'] - 273.15), 1)
# h = round(meteo['rh2m'], 1)
# meteo['rh2m'] = round(rh, 1)
# pres = round((meteo['prmslmsl'] / 100), 1)
# meteo['prmslmsl'] = round(pres, 1)


# temp = meteo['tmpprs'].to_list()
# pottemp = []
# for i in temp:
    # pottemp.append((metpy.calc.potential_temperature(850 * units.mbar, i * units.kelvin)).magnitude)

# meteo1.loc[:, 'pottemp'] = pottemp
print('\n\n\n\n\n')
print(meteo)
print('\n\n\n\n\n')


_list = meteo.index.to_list()

for i in range(len(_list)):
    _list[i] = str(_list[i])

X = _list
Y1 = meteo.iloc[:, 4]
Y2 = meteo.iloc[:, 5]
fig = plt.figure(figsize=(12,8))
ax = fig.add_subplot()
ax.plot(X, Y1, '-', color='blue')
ax.plot(X, Y2, '-', color='green')
ax.set_xticks(np.arange(0,25,5))
ax.grid()

fig.show()

input()
