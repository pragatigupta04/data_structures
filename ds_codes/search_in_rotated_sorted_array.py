# There is an integer array nums sorted in ascending order (with distinct values). 
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1<=k<nums.length) such that the resulting array is [nums[k], nums[k+1], ... nums[n-1], nums[0], nums[1], ... nums[k-1]] (0-indexed). For examplw, [0,1,2,3,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
# Given the array nums after the possible rotation and an integer
# target, return the index of target if it is in nums, or -1 if
# it is not in nums.
# You must write an algorithm with O(logn) runtime complexity.
def binarySearch(arr, n, mid, index):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        if arr[0] == n:
            return index
        else:
            return -1
    if arr[mid] == n:
        print("in if", arr, mid)
        return mid + index
    if arr[mid] > n:
        print("IN IF", arr, mid, n, mid//2)
        return binarySearch(arr[:mid], n, mid//2, index)
    else:
        print("IN ELSE", arr, mid, n, (len(arr)-mid)//2)
        return binarySearch(arr[mid:], n, (len(arr)-mid+1)//2, len(arr[:mid]))

if __name__ == "__main__":
    arr = list(map(int,input().split()))
    n = int(input())
    start = 0
    end = len(arr) - 1
    while(start <= end):
        if arr[start] > arr[end]:
            start += 1
            end -= 1
        elif start == end:
            print(start, end)
            if arr[start] > arr[start+1]:
                start += 1
            else:
                end -= 1
        else:
            break
    breakPoint = start
    print(binarySearch(arr, n, breakPoint, 0))
