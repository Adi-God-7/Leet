class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n =set(nums)
        r=[]

        for i in range(1, len(nums) + 1):
            if i not in n:
                r.append(i)
            
        return r