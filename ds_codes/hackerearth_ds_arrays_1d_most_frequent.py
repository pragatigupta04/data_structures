from collections import Counter
N = int(input()) # input the number of int
arr = list(map(int,input().split())) # input array as list
count_dict = Counter(arr) # Create a dictionary with count of every value
count_values = list(count_dict.values()) # Get all the counts
max_count_value = max(count_values) # Get max count
get_counter_for_count_dict = Counter(count_values) # Get count values for counter dict
if get_counter_for_count_dict[max_count_value] > 1:
    all_keys = [k for k,v in count_dict.items() if v == max_count_value] # Get all keys with the maximum count
    print(min(all_keys))  # Print minimum value key with maximum count
else:
    get_index = count_values.index(max_count_value) # Get index of maximum count
    key = list(count_dict.keys())[get_index] # Get key at that index
    print(key)
