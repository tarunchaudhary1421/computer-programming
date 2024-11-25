'''
Find the Missing Number in a Sequence
'''
n = int(input())
arr = list(map(int, input().split()))
for i in range(n-1): # I want to run loop till n - 1 as in one iteration i am checking two index values i.e of i and of i+1
    if arr[i+1] - arr[i] != 1:
        print(arr[i+1]-1)

