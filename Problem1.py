'''
Author@ Elijah_mikaelson
Given a list of numbers and a number k, return whether any two numbers from the list add up to k
'''
def solution(arr,k):
    for i in range(len(arr)-1):
        for j in range(len(arr)-1):
            if ((arr[i] + arr[j]) == k):

                print(str(arr[i]) + 'and' + str(arr[j]))




arr=[2,3,4,6,8,10,12,14]
k=1
solution(arr,k)




