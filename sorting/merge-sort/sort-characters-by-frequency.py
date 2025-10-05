# problem link https://leetcode.com/problems/sort-characters-by-frequency/

class Solution(object):
    def frequencySort(self, s):
        char_counts = collections.Counter(s)

        sorted_chars = sorted(char_counts.items(), key=lambda item: -item[1])

        result=[]
        for char,count in sorted_chars:
            result.append(char*count)

        return "".join(result)




        """
        :type s: str
        :rtype: str
        """
        