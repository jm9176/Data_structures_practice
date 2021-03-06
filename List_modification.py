'''
If the input list is of the form [1,2,3,4]
then the output should result in [24,12,8,6]
'''
# Finding the product of elements in a list
def prod(arr):
    var_prod = 1
    for var in arr:
        var_prod *= var

    return var_prod

# Generating the modified list
def list_gen(arr):
    var_prod = prod(arr)

    for i in range(len(arr)):
        arr[i] = int(var_prod/arr[i])

    return arr

# Input list
arr = [1, 2, 3, 4]
print (list_gen(arr))

'''
#Using numpy
import numpy as np

def list_gen(arr):
    list_prod = np.prod(arr)

    for i in range(len(arr)):
        arr[i]=int(list_prod/arr[i])

    return arr

arr = [1,2,3,4]
print(list_gen(arr))


#without div

import numpy as np

def filter_list(arr, i):
    arr.remove(arr[i])

    return np.prod(arr)

arr = [1,2,3,4]
arr_new=[]

for i in range(len(arr)):
    var = arr[i]
    arr_new.append(filter_list(arr,i))
    arr.insert(i, var)

print(arr, arr_new)
'''
