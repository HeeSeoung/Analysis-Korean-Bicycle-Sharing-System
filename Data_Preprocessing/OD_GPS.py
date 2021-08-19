import pandas as pd
import numpy as np

od = pd.read_csv('', encoding='cp949')
gps = pd.read_csv('', encoding='cp949')

arr = np.array(gps)
dict = {}

for i in range(len(arr)):
    latlon = str(arr[i, 6]) + ' ' + str(arr[i, 7])
    dict[str(arr[i, 0])] = latlon

arr = np.array(od)
temp = []

for i in range(len(arr)):

    if np.isnan(arr[i, 0]):
        temp.append(dict.get(str((arr[i, 0]))))
    else:
        temp.append(dict.get(str(int(arr[i, 0]))))

od['O_latlon'] = temp

temp = []
for i in range(len(arr)):

    if np.isnan(arr[i, 1]):
        temp.append(dict.get(str((arr[i, 1]))))
    else:
        temp.append(dict.get(str(int(arr[i, 1]))))

od['D_latlon'] = temp

od.dropna
od.to_csv('C:/Users/anhis/PycharmProjects/GPS/data/od_gps.csv')
