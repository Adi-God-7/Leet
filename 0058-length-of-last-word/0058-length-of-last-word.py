class Solution(object):
    def lengthOfLastWord(self, s):
        g=s.split()
        return len(g[-1])
        