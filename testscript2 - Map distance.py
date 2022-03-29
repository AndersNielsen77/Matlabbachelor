import csv
import os
import xlsxwriter
import numpy as np
from gmplot import gmplot
import matplotlib.pyplot as plt
import mpu

"""
For at lave sampels over distande:
1. Lave matrix over cod og RSRP
2. Fjerne nan collum or row
3. Beregne en distance fra startpunkt/mast til enkelt sample coordinat
4. Plot signal over distance
"""

array = []
array2 = []
rows = []

#file = np.genfromtxt('C:\Testsides3\Walk fra edge til kildedal st.csv', delimiter= ',')
file = np.genfromtxt('C:\Testsides3\Maalov1 Walk.csv', delimiter= ',')
#file = np.genfromtxt('C:\Testsides3\Alb Real1.csv', delimiter= ',')
#file = np.genfromtxt('C:\Testsides3\Quick maalov for switch.csv', delimiter= ',')


THDL = file[:,9] #THDL
RSRP = file[:,20] #RSRP
RSRQ = file[:,21] #RSRQ
SINR = file[:,22] #SINR

lat = file[:,57] #lat
lng = file[:,58] #lng
alt = file[:,59] #alt

''' 
THDL = THDL[~np.isnan(THDL)]
RSRP = RSRP[~np.isnan(RSRP)]
RSRQ = RSRQ[~np.isnan(RSRQ)]
SINR = SINR[~np.isnan(SINR)]
lat = lat[~np.isnan(lat)]
lng = lng[~np.isnan(lng)]
alt = alt[~np.isnan(alt)]
'''

print(RSRP)
print(lat)
print(lng)
"""""
RSRP = RSRP[1::50]
lat = lat[1::100]
lng = lng[1::100]
alt = alt[1::100]
"""

lat = np.array(lat)
lng = np.array(lng)

print(np.size(RSRP))
## 1. 
Matrix = np.vstack((lat,lng,RSRP))
Matrix = np.transpose(Matrix)
Matrix = Matrix[~np.isnan(Matrix).any(axis=1)]

# 3. 
##### Basestation location:

lat1 = 55.75150363735553
lon1 = 12.298545286568974
#lat1 = Matrix[0][0]
#lon1 = Matrix[0][1]

# Point two

distance = []
for i in range(len(Matrix)):
    lat2 = Matrix[i][0]
    lon2 = Matrix[i][1]
    dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))*1000
    distance.append(dist)


# 4. 
print(np.size(distance))
print(len(Matrix))
RSRP = Matrix[:,2]

z = np.polyfit(distance, RSRP, 1)
p = np.poly1d(z)
plt.plot(distance,p(distance),"r--")

plt.plot(distance, RSRP, 'g', label='Label 1')
plt.xlabel('Distance(Meters)')
plt.ylabel('RSRP')
plt.show()
