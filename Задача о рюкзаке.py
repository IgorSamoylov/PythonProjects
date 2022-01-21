

def bag_optimal(tr_weights: tuple, tr_cost: tuple, max_weight: int) -> int:
    items_len = len(tr_weights)
    dp = [[0] * (items_len + 1) for k in range(max_weight + 1)]
   
    for i in range(1, items_len + 1):
        for weight in range(1, max_weight + 1):
            if tr_weights[i-1] <= weight:
                dp[weight][i] = max(dp[weight][i-1], tr_cost[i-1] + dp[weight-tr_weights[i-1]][i-1])
            else:
                #print(i, weight)
                dp[weight][i] = dp[weight][i-1]

    #print(dp)
    return dp[-1][-1]

treasures_weights = (9, 3, 3, 5, 3)
treasures_costs = (15, 5, 5, 7, 6)
MaxWeight = 10
max_cost = bag_optimal(treasures_weights, treasures_costs, MaxWeight)
print(max_cost)

    
