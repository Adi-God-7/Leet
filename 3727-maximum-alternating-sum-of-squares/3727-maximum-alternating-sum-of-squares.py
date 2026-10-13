class Solution(object):
    def maxAlternatingSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        for i in range(len(nums)):
            nums[i]=nums[i]**2
        nums=sorted(nums)
       
        s=sum(nums[len(nums)//2:])
        z=sum(nums[:(len(nums)//2)])
        return s-z
        