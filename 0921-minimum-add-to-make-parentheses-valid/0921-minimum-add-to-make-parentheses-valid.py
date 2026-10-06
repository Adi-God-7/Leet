class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        size=open=0
        for i in s:
            if(i=='('):
                size+=1
            elif(size>0):
                size-=1
            else:
                open+=1
        return open+size