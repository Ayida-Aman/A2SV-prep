# problem link: https://leetcode.com/problems/minimum-window-substring/

class Solution(object):
    def minWindow(self, s, t):
        from collections import Counter
        need = Counter(t)
        need_len = len(need)
        window = {}
        l, res, res_len = 0, [-1, -1], float("inf")
        have =0
        if len(t) > len(s):
            return ""

        for r in range(len(s)):
            char = s[r]
            window[char] = window.get(char, 0) +1

            if char in need and window[char] == need[char]:
                have +=1
            
            while have == need_len:
                if (r-l+1) < res_len:
                    res = [l,r]
                    res_len = r-l +1
                
                window[s[l]] -=1

                if s[l] in need and window[s[l]] < need[s[l]]:
                    have -=1
                l+=1
        l, r = res
        return s[l:r+1] if res_len != float("inf") else ""

        
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        