# problem link: https://leetcode.com/problems/baseball-game/description/

class Solution(object):
    def calPoints(self, operations):
        record = []
        for i, op in enumerate(operations):
            if op == '+' and i>1:
                twoSum = record[-1] + record[-2]
                record.append(twoSum)
            elif op == 'D' and i>0:
                double = 2*record[-1]
                record.append(double)
            elif op == "C":
                record.pop()
            else:
                record.append(int(op))
        return sum(record)
        """
        :type operations: List[str]
        :rtype: int
        """
        