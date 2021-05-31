from numpy import *

arr1 = array([1,2,3])
arr2 = array([1,2,3])
arr3 = ([])
k = 0
for i in arr1:
    num3 = i + arr2[k]
    arr3.append(num3)
    k+=1
print(arr3)