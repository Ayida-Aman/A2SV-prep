# problem link: https://leetcode.com/problems/implement-queue-using-stacks/description/

from collections import deque
class MyQueue(object):

    def __init__(self):
        self.q = deque()

    def push(self, x):
        self.q.append(x)
        """
        :type x: int
        :rtype: None
        """
        

    def pop(self):
        return self.q.popleft()
        """
        :rtype: int
        """
        

    def peek(self):
        return self.q[0]
        """
        :rtype: int
        """
        

    def empty(self):
        return len(self.q) == 0
        """
        :rtype: bool
        """
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()