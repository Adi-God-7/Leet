class Solution(object):
    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        pg=[]
        sum=0
        cm=-1
        def gcd(a,b):
            while b!=0:
                a, b = b, a % b
            return a
        for num in nums:
            if num > cm:
                cm = num
            pg.append(gcd(num, cm))
        pg.sort()
        p=0
        q=len(pg)-1
        while p<q:
            sum+=gcd(pg[p],pg[q])
            p+=1
            q-=1
        return sum


