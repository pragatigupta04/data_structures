import math
T = int(input()) # input test cases
for i in range(T):
    N, K = map(int,input().split()) # input N and K
    arr = list(map(int,input().split())) # input arr
    sum_of_arr = sum(arr) # calculate sum
    if math.floor(sum_of_arr/N) <= K: # check if situation is already satisfying the situation
        print(0)
    else:
        p = math.floor(sum_of_arr/(K+1)) + 1 # Calculate the minimum number of elements required in the array considering the new element added is 0
        print(p-N)
