'''
Author@ Elijah_mikaelson
Given a list of numbers and a number k, return whether any two numbers from the list add up to k
'''
def Solution(arr, k):
    for i in range(0, len(arr)):
        if k - arr[i] in arr:
            return True
    return False
A = [1, 4, 45, 6, 10, 8]
n = 14
print(Solution(A, n))