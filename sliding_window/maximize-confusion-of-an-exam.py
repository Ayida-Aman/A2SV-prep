# problem link: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/

class Solution(object):
    def maxConsecutiveAnswers(self, answerKey, k):

        def max_length(char):
            l , flip, max_len = 0,0,0

            for r in range(len(answerKey)):
                if answerKey[r] != char:
                    flip+=1
                while flip > k:
                    if answerKey[l] != char:
                        flip -=1
                    l+=1
                max_len = max(max_len, r -l +1)
            return max_len
        return max(max_length("T"), max_length("F"))


        """
        :type answerKey: str
        :type k: int
        :rtype: int
        """
        