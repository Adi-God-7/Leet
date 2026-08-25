class Solution(object):
    def missingMultiple(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        i=1
        while i<=101:
            if i*k not in nums:
                return i*k
            i+=1
            
        