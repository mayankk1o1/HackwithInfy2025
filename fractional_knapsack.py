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


n, W = map(int, input().split())
items = []
for i in range(n):
    v, w = map(int, input().split())
    items.append((v, w))

print(f"{fractional_knapsack(n, W, items):.2f}")
