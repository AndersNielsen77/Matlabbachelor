import csv
import os
import xlsxwriter
import numpy as np
from gmplot import gmplot
import matplotlib.pyplot as plt



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


THDL = file[:,9] #THDL
RSRP = file[:,20] #RSRP
RSRQ = file[:,21] #RSRQ
SINR = file[:,22] #SINR

lat = file[:,57] #lat
lng = file[:,58] #lng
alt = file[:,59] #alt

THDL = THDL[~np.isnan(THDL)]
RSRP = RSRP[~np.isnan(RSRP)]
RSRQ = RSRQ[~np.isnan(RSRQ)]
SINR = SINR[~np.isnan(SINR)]
lat = lat[~np.isnan(lat)]
lng = lng[~np.isnan(lng)]
alt = alt[~np.isnan(alt)]



print(RSRP)
print(lat)
print(lng)
"""""
RSRP = RSRP[1::50]
lat = lat[1::100]
lng = lng[1::100]
alt = alt[1::100]
"""
print(np.size(RSRP))
print(np.size(lat))
print(np.size(lng))

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
print("-------------------")
print("THDL MAX: ",np.max(THDL))
print("THDL mean: ",np.mean(THDL))
print("THDL MIN: ",np.min(THDL))
print("-------------------")


RSRP = RSRP[1::50]
SINR = SINR[1::50]
print(np.size(RSRP))

x = np.arange(0, 247)


A,B = np.meshgrid(RSRP,)                                                                                      
plt.scatter(A,B)
plt.show()

#000000
#FF0000
#00FF00
#FFFFFF
#
#
#
#
