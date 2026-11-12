class Solution(object):
    def longestMonotonicSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n=len(nums)
        ans=0
        inc=1
        dec=1
        if n==1: return 1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                inc+=1
                dec=1
            elif nums[i]<nums[i-1]:
                inc=1
                dec+=1
            else:
                inc=dec=1
            ans=max(ans,dec,inc)
        return ans