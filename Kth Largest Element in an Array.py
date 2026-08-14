def find_kth_largest(nums, k):
    sorted_nums = sorted(nums, reverse=True)
    return sorted_nums[k-1]

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))

# Using heap
def find_kth_largest(nums, k):
    heap = []
    for num in nums:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)
    
    return heap[0] if heap else None

nums = [3, 2, 1, 5, 6, 4]
k = 2
print(find_kth_largest(nums, k))
