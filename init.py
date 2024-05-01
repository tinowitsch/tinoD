import pandas as pd
import numpy as np

pd.options.display.max_rows = 9999

df = pd.read_csv('data/reg.csv')

print(df.head())

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
subarr = arr[0:2, 1:3]
print(subarr)
subarr *= 2
print(arr)
#print(arr[1, 2])
print(np.sum(arr))
print(np.mean(arr, axis=1))
b = np.array([[2, 3], [4, 5], [6, 7], [8, 9]])
print(np.dot(arr, b))