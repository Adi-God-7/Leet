class Solution(object):
    def calculateScore(self, a, b):
        """:type a: int
        :type b: int
        :rtype: int
        """
        s1 = bin(a).count('1')
        s2 = bin(b).count('1')
        
        if s1 >= s2:
            return s1 * s2
        else:
            return s2 // s1