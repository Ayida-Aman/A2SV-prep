# problem link: https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/description/?envType=problem-list-v2&envId=array

# solution one (brute force)

class Solution(object):
    def minOperations(self, boxes):
        move_counter = []
        for i in range(len(boxes)):
            count, j = 0, 0
            while j<len(boxes):
                if i == j or boxes[j] == '0':
                    j+=1
                else:
                    count += abs(j-i)
                    j+=1
            move_counter.append(count)
        return move_counter
        """
        :type boxes: str
        :rtype: List[int]
        """
        