'''
Author@ Elijah_mikaelson
Given an array of integers,
return a new array such that each element at index i of the new array is the product of all
the numbers in the original array except the one at i
'''

new_array = []
def Solution(arr):
    product= 1
    for i in arr:
        product = product * i

    for j in range(len(arr)-1):
        new_value = product / arr[j]
        new_array.append(new_value)

    print(new_array)

arr=[1,2,3,4,5]
Solution(arr)


