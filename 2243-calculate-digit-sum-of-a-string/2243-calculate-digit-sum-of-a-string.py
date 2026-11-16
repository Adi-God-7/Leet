class Solution(object):
    def digitSum(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        
        n=len(s)
    
        while(n>k):
            z=""
            for i in range(0,n,k):
                z+=str(sum(int(c) for c in s[i:i+k]))
            s=z
            n=len(s)
        return s

        