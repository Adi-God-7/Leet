class Solution(object):
    def firstStableIndex(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        for i in range(len(nums)):
            if(i==0):
                mx=nums[0]
            else:
                mx=max(nums[:i])
            mn=min(nums[i:])
            if((mx-mn)<=k):
                return i
        return -1