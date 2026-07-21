class Solution(object):
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        m=[]
        def mn(nums):
            l=[]
            while nums!=0:
                l.append(nums%10)
                nums//=10
            return max(l)
        for i in nums:
            m.append(mn(i))
        
        ans=-1

        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if m[i]==m[j]:
                    ans=max(ans,nums[i]+nums[j])

        return ans
        