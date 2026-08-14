def find_second_largest(arr):
    if len(arr) < 2:
        return None

    first = second = float('-inf')
    for num in arr:
        if num > first:
            second, first = first, num
        elif first > num > second:
            second = num
    
    return second if second != float('-inf') else None

# Example usage
arr = [5, 7, 8, 8, 6, 4, 7]
second_largest = find_second_largest(arr)
print("The second largest element is:", second_largest)
