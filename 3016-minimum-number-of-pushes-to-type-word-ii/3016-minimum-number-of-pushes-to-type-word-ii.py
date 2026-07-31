class Solution(object):
    def minimumPushes(self, word):
        """
        :type word: str
        :rtype: int
        """
        f=[0]*26
        for c in word:
            f[ord(c)-ord("a")]+=1
        f.sort(reverse=True)
        tp=0
        for i in range(26):
            if f[i]==0:
                break
            tp+=(i//8 +1)*f[i]
        return tp
        