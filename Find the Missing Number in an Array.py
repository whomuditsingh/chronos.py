def missing_number(arr):
    n = len(arr)
    total_sum = n * (n + 1) // 2
    return total_sum - sum(arr)

arr = [3, 0, 1]
print(missing_number(arr))

# Another approach with xor
def missing_number(arr):   
    n = len(arr)
    xor_sum = n
    for i in range(n):
        xor_sum ^= i ^ arr[i]
    return xor_sum

# Example usage
arr = [3, 0, 1]
print(missing_number(arr))
