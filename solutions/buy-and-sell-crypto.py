# https://www.youtube.com/watch?v=5WZl3MMT0Eg

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        current_profit = 0

        for i in range(1, len(prices)):
            change = current_profit + (prices[i] - prices[i - 1])
            current_profit = 0 if change < 0 else change
            max_profit = current_profit if max_profit < current_profit else max_profit

        return max_profit
