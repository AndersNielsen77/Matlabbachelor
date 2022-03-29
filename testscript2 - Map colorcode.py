import csv
import os
import xlsxwriter
import numpy as np
from gmplot import gmplot
import matplotlib.pyplot as plt
import mpu

array = []
array2 = []
rows = []
lat0 = []
lat70 = []
lat80 = []
lat90 = []
lat100 = []
lat110 = []
lat120 = []
lats = []
lng0 = []
lng70 = []
lng80 = []
lng90 = []
lng100 = []
lng110 = []
lng120 = []
lngs = []
#file = np.genfromtxt('C:\Testsides3\Walk fra edge til kildedal st.csv', delimiter= ',')
file = np.genfromtxt('C:\Testsides3\Maalov1 Walk.csv', delimiter= ',')
#file = np.genfromtxt('C:\Testsides3\Alb Real1.csv', delimiter= ',')
#file = np.genfromtxt('C:\Testsides3\Quick maalov for switch.csv', delimiter= ',')
#file = np.genfromtxt('C:\Testsides3\Tog.csv', delimiter= ',')



THDL = file[:,9] #THDL
RSRP = file[:,20] #RSRP
RSRQ = file[:,21] #RSRQ
SINR = file[:,22] #SINR

lat = file[:,57] #lat
lng = file[:,58] #lng
alt = file[:,59] #alt

trans = file[:,68] #trans


THDL = THDL[~np.isnan(THDL)]
RSRP = RSRP[~np.isnan(RSRP)]
RSRQ = RSRQ[~np.isnan(RSRQ)]
SINR = SINR[~np.isnan(SINR)]
lat = lat[~np.isnan(lat)]
lng = lng[~np.isnan(lng)]
alt = alt[~np.isnan(alt)]
trans = trans[~np.isnan(trans)]




print(RSRP)
print(lat)
print(lng)
print(trans)
"""""
RSRP = RSRP[1::50]
lat = lat[1::100]
lng = lng[1::100]
alt = alt[1::100]
"""
print(np.size(RSRP))
print(np.size(lat))
print(np.size(lng))
print(np.size(trans))

gmap3 = gmplot.GoogleMapPlotter(55.751071, 12.297769, 15)

for i in range(np.size(RSRP)):
    #if np.isnan(RSRP):
    #    lat0 = lat[i]
    #    lng0 = lng[i]
    #print(RSRP[i])
    if (RSRP[i] > -70): #mindre end 70
        lat70.append(lat[i])
        lng70.append(lng[i])
    elif (RSRP[i] > -80):
        lat80.append(lat[i])
        lng80.append(lng[i])
    elif (RSRP[i] > -90):
        lat90.append(lat[i])
        lng90.append(lng[i])
    elif (RSRP[i] > -100):
        lat100.append(lat[i])
        lng100.append(lng[i])
    elif (RSRP[i] > -110):
        lat110.append(lat[i])
        lng110.append(lng[i])
    elif (RSRP[i] > -120):
        lat120.append(lat[i])
        lng120.append(lng[i])
    else:
        lats.append(lat[i])
        lngs.append(lng[i])

#gmap3.scatter( lat0, lng0, '#FF00DB', marker = True )
gmap3.scatter( lat70, lng70, '#FF0000', marker = True ) #Rød
gmap3.scatter( lat80, lng80, '#FFA500', marker = True ) # Orange
gmap3.scatter( lat90, lng90, '#FFFF00', marker = True ) # GUL
gmap3.scatter( lat100, lng100, '#00FF00', marker = True ) # Grøn
gmap3.scatter( lat110, lng110, '#00FFFF', marker = True ) #Aqua
gmap3.scatter( lat120, lng120, '#0000FF', marker = True ) #Blå
gmap3.scatter( lats, lngs, '#000000', marker = True )



#gmap3.scatter( lat, lng, '#FF0000', marker = True )
gmap3.plot(lat, lng, 'cornflowerblue', edge_width = 2.5)
gmap3.draw( "C:\Testsides3\map13.html")

print("-------------------")
print("RSRP MAX: ",np.min(RSRP))
print("RSRP mean: ",np.mean(RSRP))
print("RSRP MIN: ",np.max(RSRP))
print("-------------------")
print("RSRQ MAX: ",np.min(RSRQ))
print("RSRQ mean: ",np.mean(RSRQ))
print("RSRQ MIN: ",np.max(RSRQ))
print("-------------------")
print("SINR MAX: ",np.max(SINR))
print("SINR mean: ",np.mean(SINR))
print("SINR MIN: ",np.min(SINR))
print("-------------------")
print("THDL MAX: ",np.max(THDL))
print("THDL mean: ",np.mean(THDL))
print("THDL MIN: ",np.min(THDL))
print("-------------------")
print("Trans MAX: ",np.max(trans))
print("Trans mean: ",np.mean(trans))
print("Trans MIN: ",np.min(trans))
print("-------------------")


RSRP = RSRP[1::1]
SINR = SINR[1::1]
print(np.size(RSRP))

"""
lat1 = 52.2296756
lon1 = 21.0122287

# Point two
lat2 = 52.406374
lon2 = 16.9251681

# What you were looking for
dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))
print(dist)
"""
X = range(0,np.size(RSRP))


z = np.polyfit(X, RSRP, 1)
p = np.poly1d(z)
plt.plot(X,p(X),"r--")

plt.plot(X, RSRP, 'g', label='Label 1')
plt.show()

"""
For at lave sampels over distande:
1. Lave matrix over cod og RSRP
2. Fjerne nan collum or row
3. Beregne en distance fra startpunkt/mast til enkelt sample coordinat
4. Plot signal over distance
"""