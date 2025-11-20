# problem link: https://leetcode.com/problems/pascals-triangle/description/?envType=problem-list-v2&envId=array


class Solution(object):
    def generate(self, numRows):
        Ptriangle = []
        for i in range (numRows):   
            row = [1]

            if Ptriangle:
                prevRow = Ptriangle[-1]
                for j in range(1, len(prevRow)):
                    row.append(prevRow[j-1] + prevRow[j])
                row.append(1)
            Ptriangle.append(row)
        return Ptriangle
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
