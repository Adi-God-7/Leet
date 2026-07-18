class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        s=sorted(nums)
        n=len(nums)+1
        r=[]
        for i in range(1,len(nums)):
            if(s[i-1]==s[i]):
                r.append(s[i])
        s=sum(set(nums))
        s1=(n*(n-1))/2
        r.append(int(s1-s))
        return r