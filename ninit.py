import numpy as np
import math as mp
from numpy import random

x = random.randint(100)
y = random.rand()
z = random.randint(100, size=(5))
print(z)
print(x)
print(y)

arr = np.array([1, 2, 3, 4, 5])
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[1, 2], [3, 4], [5, 6]])


def equalArr(a, b):
    if a is b:
        return True
    else:
        return False


print(arr)
print(arr1)

print(equalArr(arr, arr1))

print(type(arr))
print(type(arr1))
