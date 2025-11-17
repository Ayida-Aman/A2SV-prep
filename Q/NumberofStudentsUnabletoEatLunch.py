# problem link: https://leetcode.com/problems/number-of-students-unable-to-eat-lunch/description/

# attempt 1 (usig Q)
from collections import deque
class Solution(object):
    def countStudents(self, students, sandwiches):
        studentsQ = deque(students)
        sandwichesQ = deque(sandwiches)
        count =0
        while studentsQ and sandwichesQ:
            if studentsQ[0] == sandwichesQ[0]:
                studentsQ.popleft()
                sandwichesQ.popleft()
                count = 0
            else:
                studentsQ.append(studentsQ.popleft())
                count +=1
            if count == len(studentsQ):
                break
        return (count)

        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        