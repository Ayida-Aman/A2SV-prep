# problem link: https://leetcode.com/problems/clear-digits/description/

class Solution(object):
    def clearDigits(self, s):
        newS = []

        for char in s:
            if char.isdigit():
                if newS:
                    newS.pop()
            else:
                newS.append(char)
        return ''.join(newS)
        """
        :type s: str
        :rtype: str
        """
        