# Minimum Number of Coins
# Description:
# Given an amount and coin denominations, find the minimum number of coins needed to make the amount.
# Input Format:
# amount
# denominations (space-separated)
# Output Format:
# Minimum number of coins
# Sample Input:
# 93
# 1 2 5 10 20 50 100
# Sample Output:
# 4
# Greedy Approach:
# Sort denominations in descending order. Pick the largest denomination possible until the amount is zero.

def min_coins(amount, denomination):
    denomination.sort()
    count = 0
    for i in range(len(denomination) - 1, -1, -1):
        while amount >= denomination[i]:
            amount -= denomination[i]
            count += 1
    return count

#Input Format
amount = int(input("Enter Amount: "))
denomination = list(map(int, input("Enter denominations (space-separated): ").split()))
print(min_coins(amount, denomination))
