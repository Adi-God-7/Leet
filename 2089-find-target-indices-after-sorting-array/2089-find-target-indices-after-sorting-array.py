class Solution(object):
    def targetIndices(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        c= 0
        tc = 0

        for num in nums:
            if num < target:
                c+= 1
            elif num == target:
                tc += 1


        return list(range(c,c+ tc))