def find_duplicates(arr):
    visited = set()
    duplicates = set()
    for num in arr:
        if num in visited:
            duplicates.add(num)
        else:
            visited.add(num)
    return list(duplicates)

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr))

# Another solution with dictionary
from collections import defaultdict
def find_duplicates(arr):
    res = []
    freq_map = defaultdict(int)
    for num in arr:
        freq_map[num] += 1
        if freq_map[num] > 1:
            res.append(num)
    
    return res

arr = [4, 3, 2, 7, 8, 2, 3, 1]
print(find_duplicates(arr))
