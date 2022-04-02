"""
    Platform: LeetCode

    Link to Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

    Problem Statement: You are given an array prices where prices[i] is the price of a given stock on the ith day.
    You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
    Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    Example 1:

    Input: prices = [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
    Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

    Example 2:

    Input: prices = [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transactions are done and the max profit = 0.    

    Constraints:

    1 <= prices.length <= 105
    0 <= prices[i] <= 104
"""

class MaximizeStockProfit:
    def __init__(self) -> None:
        pass
    
    # The idea is to maximize the profit from selling the stocks.
    # For that, start with considering max profit as 0 and min price
    # as the first item in the prices list. Loop over the remaining
    # list, and update min prices whenever the price is lower than
    # the current min price. Otherwise, set max profit to whichever
    # is larger between the current max profit 
    # or (current price - current min price).
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
                continue
            
            max_profit = max(max_profit, prices[i] - min_price)
            
        return max_profit

prices_arr = [7,1,5,3,6,4]

maxProfitObj = MaximizeStockProfit()
print(maxProfitObj.maxProfit(prices_arr))