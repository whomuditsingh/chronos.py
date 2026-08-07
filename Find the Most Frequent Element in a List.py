from collections import defaultdict
def most_frequent(arr):
    freq_map = defaultdict(int)
    res = None
    curr_max_freq = -1
    for num in arr:
        freq_map[num] += 1
        if freq_map[num] > curr_max_freq:
            res = num
            curr_max_freq = freq_map[num]
    return res

arr = [1, 3, 2, 1, 2, 2, 3, 3, 3, 1]
print(most_frequent(arr)) 

# Same with less code and built in function
def most_frequent(arr): 
    return max(set(arr), key=arr.count)
arr = [1, 3, 2, 1, 2, 2, 3, 3, 3, 1]
print(most_frequent(arr))
