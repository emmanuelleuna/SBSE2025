def max_subarray_sum(arr):
    if not arr:
        return 0, []
    
    max_sum = float('-inf')
    current_sum = 0
    start = end = s = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = s
            end = i
        
        if current_sum < 0:
            current_sum = 0
            s = i + 1
    
    return max_sum, arr[start:end+1]

# Example usage
test_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
max_sum, subarray = max_subarray_sum(test_array)
print("Maximum Subarray Sum:", max_sum)
print("Subarray:", subarray)
