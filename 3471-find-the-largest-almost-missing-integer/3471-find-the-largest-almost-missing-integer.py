class Solution(object):
    def largestInteger(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        length = len(nums)
        freq = [0] * 51

        for i in range(0, length-k+1):
            subarray = set(nums[i:i+k])
            for num in subarray:
                freq[num] += 1
        
        ans = -1

        for i in range(50, -1, -1):
            if freq[i] == 1:
                return i
        
        return ans