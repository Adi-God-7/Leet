class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        n=len(s)
        res=0
        c=0
        i=0
        while(i<n):
            if(s[i]=='('):
                c+=1
                i+=1
            else:
                if(c>0):
                    c-=1
                else:
                    res+=1
                if(i+1<n and s[i+1]==')'):
                    i+=2
                else:
                    res+=1
                    i+=1
        return res+c*2

