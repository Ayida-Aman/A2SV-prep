# problem link: https://leetcode.com/problems/watering-plants-ii/description/

class Solution(object):
    def minimumRefill(self, plants, capacityA, capacityB):
        capA = capacityA
        capB = capacityB
        counter, i = 0,0
        j = len(plants) -1
        while i <= j:
            if j==i:
                if max(capA, capB) < plants[i]:
                    counter +=1
                break
            if capA < plants[i]:
                capA = capacityA
                counter +=1
            capA -=plants[i]
            i+=1

            if capB < plants[j]:
                capB = capacityB
                counter +=1
            capB -=plants[j]
            j -=1
                
        return counter



        """
        :type plants: List[int]
        :type capacityA: int
        :type capacityB: int
        :rtype: int
        """
        