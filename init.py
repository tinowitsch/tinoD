import pandas as pd
import numpy as np
import math
import Rectangle as nyRect

pd.options.display.max_rows = 9999

try:
    df = pd.read_csv('data/reg.csv')
    print(df.head())
    print(math.sqrt(81))
    print(math.pow(2, 3))
    print(math.isnan(2.2))
    df.close()
except FileNotFoundError:
    print('File not found.')

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
subarr = arr[0:2, 1:3]
print(subarr)
subarr *= 2
print(arr)
# print(arr[1, 2])
print(np.sum(arr))
print(np.mean(arr, axis=1))
b = np.array([[2, 3], [4, 5], [6, 7], [8, 9]])
print(np.dot(arr, b))

r1 = nyRect.Rectangle(10, 20)
print(r1.get_area())
print(r1.get_perimeter())
print(r1.get_diagonal())
print(r1.get_picture())
print(r1.get_amount_inside(r1))
print(r1)
r2 = nyRect.Rectangle(200, 100)
print(r2.get_picture())
print(r2.get_amount_inside(r1))