def longest_substring(s):
    char_index_map = {}
    start = 0
    max_len = 0

    for idx, char in enumerate(s):
        if char in char_index_map and char_index_map[char] >= start:
            start = char_index_map[char] + 1
        char_index_map[char] = idx
        max_len = max(max_len, idx - start + 1)

    return max_len

s = "abcabcbb"
print(longest_substring(s))

# Another approach
def longest_substring(s):
    left = 0
    visited = set()
    res = 0
    for idx, char in enumerate(s):
        while char in visited:
            visited.remove(s[left])
            left += 1

        visited.add(char)
        res = max(res, len(visited))
    return res

s = "abcabcbb"
print(longest_substring(s))
