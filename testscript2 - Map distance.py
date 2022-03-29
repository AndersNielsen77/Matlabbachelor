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
#file = np.genfromtxt('C:\Testsides3\Maalov1 Walk.csv', delimiter= ',')
file = np.genfromtxt('C:\Testsides3\Alb Real1.csv', delimiter= ',')
#file = np.genfromtxt('C:\Testsides3\Quick maalov for switch.csv', delimiter= ',')
#file = np.genfromtxt('C:\Testsides3\Tog.csv', delimiter= ',')



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

#lat1 = 55.75150363735553
#lon1 = 12.298545286568974
lat1 = Matrix[0][0]
lon1 = Matrix[0][1]

# Point two

distance = []
for i in range(len(Matrix)):
    lat2 = Matrix[i][0]
    lon2 = Matrix[i][1]
    dist = mpu.haversine_distance((lat1, lon1), (lat2, lon2))*1000
    distance.append(dist)


# 4. 
print("test",np.max(distance))
print(len(Matrix))
RSRP = abs(Matrix[:,2])

def diffpath(distance,lambda1,h):
    d1 = distance/2
    d2 = distance/2
    v = h*(np.sqrt(2*(d1+d2)/(lambda1*d1*d2)))
    if v <= -1:
        Diffraction=0
    elif v <= 0:
        Diffraction=20*np.log10(0.5-0.62*v)
    elif v <= 1:
        Diffraction=20*np.log10(0.5*np.exp(-0.95*v))
    elif v <= 2.4:
        test2 = (0.38-0.1*v)**2
        test = np.sqrt(0.1184-(test2))
        Diffraction=20*np.log10(0.4-(test))
    else:
        Diffraction=20*np.log10(0.225/v)
    return Diffraction

xrange = np.linspace(0,np.max(distance),np.size(distance))
Wavelength = 0.085654988
K1 = 28.3
K2 = 44.9
K3 = 5.83
K4 = 0.5
K5 = -6.55
TXheight = 25
RXheight = 1.5
AntennaGainTx = 15
AntennaGainRx = 5
HTeff = TXheight


Transmiterpower=53

funk3array = []
for i in range(len(xrange)):
    DiffractionLoss = diffpath(xrange[i],Wavelength,TXheight-20)
    funk3 = K1+K2*np.log10(xrange[i])+K3*np.log10(HTeff)+K4*DiffractionLoss+K5*np.log10(xrange[i])*np.log10(HTeff)
    funk3array.append(funk3)
    
funk1 = 20*np.log10(xrange)+20*np.log10(3500)-27.55
funk2 = 20*np.log10(4*np.pi*1/Wavelength)+10*2.16*np.log10(xrange/1)+1.7


z = np.polyfit(distance, RSRP, 1)
p = np.poly1d(z)
plt.plot(distance, p(distance),"r--")
plt.plot(distance, funk1, 'r',label='Free path loss')
plt.plot(distance, funk2, 'g',label='CL path loss')
plt.plot(distance, funk3array, 'y',label='SPM path loss')

plt.plot(distance, RSRP, 'b', label='Label 1')
plt.ylim([60, 150])
plt.xlabel('Distance(Meters)')
plt.ylabel('RSRP')
plt.show()
