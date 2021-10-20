# Given an array Arr of N positive integerss. Your task is to find
# the elements whose value is equal to that of its index value
# (consider 1-based ondexing)
Arr = list(map(int, input().split()))
outputArr = []
for index in range(len(Arr)):
    if index+1 == Arr[index]:
        outputArr.append(index+1)
print(outputArr)
