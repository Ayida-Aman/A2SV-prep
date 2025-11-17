# problem link: https://leetcode.com/problems/time-needed-to-buy-tickets/description/

from collections import deque
class Solution(object):
    def timeRequiredToBuy(self, tickets, k):
        count = 0
        q = deque([(i, t) for i, t in enumerate(tickets)])
        while q:
            index, ticket = q.popleft()
            ticket -=1
            count +=1
            if ticket>0:
                q.append((index, ticket))
            elif index == k:
                break
        return count
        """
        :type tickets: List[int]
        :type k: int
        :rtype: int
        """
        