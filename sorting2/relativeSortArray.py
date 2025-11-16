# problem link: https://leetcode.com/problems/relative-sort-array/description/?envType=problem-list-v2&envId=array

# attempt 1 (accepted but not efficient)

class Solution(object):
    def relativeSortArray(self, arr1, arr2):

        freq = {}
        leftOvers = []
        arr3 = []
        arr2Set = set(arr2)
        for num in arr1:
            if num in arr2Set:
                if num in freq:
                    freq[num] +=1
                else:
                    freq[num] = 1
            else:
                leftOvers.append(num)
        for num in arr2:
            while freq[num] > 0:
                arr3.append(num)
                freq[num] -=1
        for i in range(len(leftOvers)):
            j =i
            while j>0 and leftOvers[j] < leftOvers[j-1]:
                leftOvers[j-1],leftOvers[j] = leftOvers[j], leftOvers[j-1] 
                j-=1
        return arr3 + leftOvers

        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """


# attempt 2 (use the built in method)

class Solution(object):
    def relativeSortArray(self, arr1, arr2):

        freq = {}
        leftOvers = []
        arr3 = []
        arr2Set = set(arr2)
        for num in arr1:
            if num in arr2Set:
                if num in freq:
                    freq[num] +=1
                else:
                    freq[num] = 1
            else:
                leftOvers.append(num)
        for num in arr2:
            while freq[num] > 0:
                arr3.append(num)
                freq[num] -=1
        leftOvers.sort()
        return arr3 + leftOvers

        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        