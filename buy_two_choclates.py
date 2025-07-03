def buy_chocolates(prices, money):
    min1 = float('inf')
    min2 = float('inf')
    for price in prices:
        if price < min1:
            min2 = min1
            min1 = price
        elif price < min2:
            min2 = price
    total_cost = min1 + min2
    if total_cost > money:
        return money
    else:
        return money - total_cost

no_of_chocolates = int(input("Enter number of chocolates you want to add: "))
money = int(input("Enter Money: "))
prices = []
for i in range(no_of_chocolates):
    price = int(input(f"Enter price of chocolate {i + 1}: "))
    prices.append(price)
print("Money left after purchase:", buy_chocolates(prices, money))
