'''
Count the Frequency of Elements
'''
n = int(input())
n_arr = list(map(int, input().split()))
# c = set(n_arr)
for i in set(n_arr):
    print(f'{i}:{n_arr.count(i)}')    