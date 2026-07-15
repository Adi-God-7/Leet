class Solution(object):
    def sumAndMultiply(self, n):
        x=0
        s=0
        q=str(n)
        for i in q:
            if(i!='0'):
                x=x*10+int(i)
                s=s+int(i)
        return x*s