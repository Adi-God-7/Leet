class Solution(object):
    def missingInteger(self, nums):
        n=len(nums)

        s=nums[0]

        for i in range(1,n):
            if nums[i]==nums[i-1]+1:
                s+=nums[i]
            else:
                break

        m=s

        while m in nums:
            m+=1

        return m