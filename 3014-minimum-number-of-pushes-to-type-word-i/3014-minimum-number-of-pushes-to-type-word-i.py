class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        n=len(word)
        if(n<=8):
            return n
        if(n>8 and n<=16):
            return (n-8)*2+8
        if(n>16 and n<=24):
            return (n-16)*3+24
        if(n>24 and n<=26):
            return (n-24)*4+48
        