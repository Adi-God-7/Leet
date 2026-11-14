class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        """
        :type nums: List[int]
        :type l: int
        :type r: int
        :rtype: int
        """
        mi=float('inf')
        n=len(nums)
        for i in range(n):
            s=0
            for j in range(i,n):
                s+=nums[j]
                length=j-i+1
                if l<=length<=r and s>0:
                    mi=min(mi,s)
        return -1 if mi==float('inf') else mi

