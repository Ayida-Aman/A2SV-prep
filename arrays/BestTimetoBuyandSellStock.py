# problem link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/submissions/1826861560/?envType=problem-list-v2&envId=array

# attempt 1

# class Solution(object):
#     def maxProfit(self, prices):

#         for i, price in enumerate(prices):
#             pricesArr = prices[i: len(prices)]
#             maximum = max(pricesArr)
#             minimum = min (pricesArr)
#             if prices.index(minimum) < prices.index(maximum):
#                 return maximum - minimum
#         return 0

# attempt 2

# class Solution(object):
#     def maxProfit(self, prices):
#         diff = []
#         for i, price in enumerate(prices):
#             if i + 1 < len(prices):
#                 maximum = max(prices[i+1:])
#                 if maximum > price:
#                     diff.append(maximum - price)

#         return max(diff) if len(diff) > 0 else 0

# attempt 3 (accepted)

class Solution(object):
    def maxProfit(self, prices):
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)
        return max_profit

        """
        :type prices: List[int]
        :rtype: int
        """
        