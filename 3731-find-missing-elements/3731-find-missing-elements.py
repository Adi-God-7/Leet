class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        m1=min(nums)
        m2=max(nums)
        res=[]
        for i in range(m1,m2+1):
            if(i not in  nums):
                res.append(i)
        return res

        