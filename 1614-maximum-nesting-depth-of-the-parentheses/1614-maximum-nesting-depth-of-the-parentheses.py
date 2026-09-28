class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        mx=0
        c=0
        for i in s:
            if(i=='('):
                c+=1
                mx=max(mx,c)
            elif(i==')'):
                c-=1
        return mx