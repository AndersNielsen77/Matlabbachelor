import csv
import xlsxwriter
import numpy as np
array = []
array2 = []
rows = []
for i in range(34):
    file = np.genfromtxt(str(i)+'.csv', delimiter= ',')
    file = file[:,11] #SS-RSRP
#    file = file[:,12] #SS-RSRQ
#    file = file[:,13] #SS-SINR
    file = file[~np.isnan(file)]
    mean = np.mean(file)
    std = np.std(file)
    array.append(mean)
    array2.append(std)
array2 = np.absolute(array2)
array = np.absolute(array)

b = array[::2]
c = array[1::2]
b2 = array2[::2]
c2 = array2[1::2]
print(b)
print(c)

workbook = xlsxwriter.Workbook('output.xlsx')
worksheet = workbook.add_worksheet()
row = 0
col = 0

for j in range(len(b)):
    worksheet.write(0, j, c[j])
    worksheet.write(1, j, b[j])


for j in range(len(b2)):
    worksheet.write(3, j, c2[j])
    worksheet.write(4, j, b2[j])
workbook.close()