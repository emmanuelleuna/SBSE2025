def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last_merged = merged[-1]
        if current[0] <= last_merged[1]:  # Overlapping intervals
            merged[-1] = (last_merged[0], max(last_merged[1], current[1]))
        else:
            merged.append(current)
    
    return merged

# Example usage
test_intervals = [(7, 8), (1, 5), (2, 4), (4, 6)]
merged_result = merge_intervals(test_intervals)
print("Merged intervals:", merged_result)
