import csv
import xlsxwriter
import numpy as np
import gmplot


array = []
array2 = []
rows = []
file = np.genfromtxt('C:\Testsides3\Alb Real1.csv', delimiter= ',')

lat = file[:,57] #lat
lng = file[:,58] #lng
alt = file[:,59] #alt

lat = lat[~np.isnan(lat)]
lng = lng[~np.isnan(lng)]
alt = alt[~np.isnan(alt)]

print(lat)
print(lng)

lat = lat[1::100]
lng = lng[1::100]
alt = alt[1::100]

print(np.size(lat))
print(np.size(lng))

gmap3 = gmplot.GoogleMapPlotter(55.657003, 12.335542, 15)

gmap3.scatter( lat, lng, '#00FFFF', marker = True )

#gmap3.scatter( lat, lng, '#FF0000', marker = True )
gmap3.plot(lat, lng, 'cornflowerblue', edge_width = 2.5)
gmap3.draw( "C:\Testsides3\map13.html")