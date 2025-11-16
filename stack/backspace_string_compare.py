# problem link: https://leetcode.com/problems/backspace-string-compare/description/

class Solution(object):
    def backspaceCompare(self, s, t):
        newS , newT = [], []

        for char in s:
            if char == '#':
                if len(newS) > 0:
                    newS.pop()
            else:
                newS.append(char)
        for char in t:
            if char == '#':
                if len(newT) > 0:
                    newT.pop()
            else:
                newT.append(char)

        return newS == newT
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        