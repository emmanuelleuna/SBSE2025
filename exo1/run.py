def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            left = mid + 1 
        else:
            right = mid - 1 
    return -1 

# Test 
sorted_list = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
print(binary_search(sorted_list, 7))  # Output: 3
print(binary_search(sorted_list, 10)) # Output: -1
