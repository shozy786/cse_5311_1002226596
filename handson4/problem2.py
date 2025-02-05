def dedupe(array): # Dedupe is a word used for deduplication
    result = []
    for i in array:
        if len(result) == 0 or result[-1] != i:
            result.append(i)

    return result

# Test Case 1
print(dedupe([2, 2, 2, 2, 2]))

# Test Case 2
print(dedupe([1, 2, 2, 3, 4, 4, 4, 5, 5]))