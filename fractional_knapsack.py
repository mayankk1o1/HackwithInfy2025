# Fractional Knapsack Problem
# Description:
# Given n items with values and weights, and a knapsack with capacity W, find the maximum value you can obtain. You can take fractions oInput Format:
# n W
# value1 weight1
# value2 weight2
# ...
# valuen weightn
# Output Format:
# Maximum value (2 decimal places)
# Sample Input:
# 3 50
# 60 10
# 100 20
# 120 30
# Sample Output:
# 240.00
# Greedy Approach:
# Sort items by value/weight ratio. Take as much as possible from the highest ratio item

def fractional_knapsack(n, W, items):
    items = [(v, w, v / w) for v, w in items]
    items.sort(key=lambda x: x[2], reverse=True)
    total_value = 0.0
    for value, weight, ratio in items:
        if W == 0:
            break
        if weight <= W:
            total_value += value
            W -= weight
        else:
            total_value += ratio * W
            break
    return total_value

#Input Format:
n, W = map(int, input().split())
items = []
for i in range(n):
    v, w = map(int, input().split())
    items.append((v, w))

print(f"{fractional_knapsack(n, W, items):.2f}")
