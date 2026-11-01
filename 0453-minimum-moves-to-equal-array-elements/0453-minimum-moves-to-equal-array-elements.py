class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        mn=min(nums)
        c=0
        for i in nums:
            if(i!=mn):
                c+=abs(i-mn)
        return c
        