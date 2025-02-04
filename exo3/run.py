def knapsack(items, max_weight):
    n = len(items)
    dp = [[0] * (max_weight + 1) for _ in range(n + 1)]
    
    for i in range(1, n + 1):
        value, weight = items[i - 1]
        for w in range(max_weight + 1):
            if weight <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - weight] + value)
            else:
                dp[i][w] = dp[i - 1][w]
    
    # Backtracking to find the selected items
    w = max_weight
    selected_items = []
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(items[i - 1])
            w -= items[i - 1][1]
    
    return dp[n][max_weight], selected_items[::-1]

# Example usage
items = [(60, 10), (100, 20), (120, 30)]  # (value, weight)
max_weight = 50
max_value, selected = knapsack(items, max_weight)
print("Maximum value:", max_value)
print("Selected items:", selected)