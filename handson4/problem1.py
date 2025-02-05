def merge_sorted(arr, K, N):#takes 2D array of sorted arrays
    result = []
    counters = [0 for i in range(K)]
    while min(counters) < N:
        min_value = 99999999
        min_idx = -1
        for idx, counter in enumerate(counters):
            if counter >= N:
                continue
            if arr[idx][counter] <= min_value:
                min_value = arr[idx][counter]
                min_idx = idx
        result.append(min_value)
        counters[min_idx] += 1
    return result
# Test Case 1
arr = [
    [1,3,5,7],
    [2,4,6,8],
    [0,9,10,11]
]
print(merge_sorted(arr, 3, 4))
# Test Case 2
arr = [[1,3,7],
[2,4,8],
[9,10,11]]

print(merge_sorted(arr, 3, 3))
