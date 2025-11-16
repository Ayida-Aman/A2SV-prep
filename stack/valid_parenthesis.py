# problem link: https://leetcode.com/problems/valid-parentheses/description/

class Solution(object):
    def isValid(self, s):

        open_brackets = []

        for char in s:
            if char == "(" or char == "[" or char == "{":
                open_brackets.append(char)
            elif len(open_brackets) > 0:
                c = open_brackets.pop()
                if char == ")" and c != "(":
                    return False
                if char == "]" and c != "[": 
                    return False
                if char == "}" and c != "{": 
                    return False
            else:
                return False
        return len(open_brackets) == 0
        """
        :type s: str
        :rtype: bool
        """
        