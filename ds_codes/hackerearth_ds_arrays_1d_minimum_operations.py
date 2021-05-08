N = int(input()) # Input N
A = list(map(int, input().split(" "))) # input array
count = 0 # initialize count to 0
prev = -1 # initialize previous to -1
for i in range(N): # check for all the elements in the array,  count 1 for consequent same values
    if A[i] != prev:
        count += 1
    prev = A[i]
print(count)
