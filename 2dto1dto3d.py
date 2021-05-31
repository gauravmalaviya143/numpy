from numpy import *
arr1 = array([
                [1,2,3,6,2,9,1,2],
                [4,5,6,7,5,3,1,2]
            ])
arr2 = arr1.flatten()
arr3 = arr2.reshape(2,2,4)
print(arr2)
print(arr3)