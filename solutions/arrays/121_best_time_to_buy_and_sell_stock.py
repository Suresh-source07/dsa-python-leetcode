"""
Problem: Best Time to Buy and Sell Stock (LeetCode 121)
Approach: Track minimum price so far
Time Complexity: O(n)
Space Complexity: O(1)
"""

def max_profit(prices):
    min_price = prices[0]
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)

    return max_profit

if __name__ == "__main__":
    print(max_profit([7,1,5,3,6,4]))
