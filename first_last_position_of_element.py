# Given a sorted array arr containing n elements with possibly
# duplicate elements, the task is to find indexes of first and last
# occurrences of an element x in the given array.
values = list(map(int, input().split()))
element = int(input())
start = 0
end = len(values) - 1
start_pos = -1
end_pos = -1
while(start < end):
    if values[start] == element:
        if start_pos == -1:
            start_pos = start
        else:
            end_pos = start
        start += 1
    elif values[end] == element:
        if end_pos == -1:
            end_pos = end
        else:
            start_pos = end
        end -= 1
    else:
        if start_pos != -1 and end_pos != -1:
            break
        elif start_pos != -1 and end_pos == -1:
            end_pos = start_pos
        elif end_pos != -1 and start_pos == -1:
            start_pos = end_pos
        elif element > values[start]:
            start += 1
        else:
            end -= 1
print("Starting position : ", start_pos)
print("Ending position : ", end_pos)
        
        
