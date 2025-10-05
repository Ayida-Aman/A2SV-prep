# problem link https://leetcode.com/problems/maximum-number-of-coins-you-can-get/

class Solution(object):
    def maxCoins(self, piles):

        n = len(piles)
        x = n//3
        piles.sort()

        new_piles = piles[x : n]
        results = 0
        for i in range(0,len(new_piles), 2):
            results += new_piles[i]
        return results
        """
        :type piles: List[int]
        :rtype: int
        """
        