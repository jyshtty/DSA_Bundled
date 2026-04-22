class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        mini = prices[0]
        max_profit = 0

        for idx in range(1, len(prices)):

            if prices[idx] < mini:
                mini = prices[idx]
            else:
                max_profit = max(max_profit, prices[idx] - mini)
        
        return max_profit


        