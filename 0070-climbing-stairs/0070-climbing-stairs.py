class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        cur=1
        pos=1
        for i in range(1,n):
            cur,pos=cur+pos,cur
        return cur