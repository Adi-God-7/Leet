class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        m=[]
        for i in matrix:
            m.extend(i)
        l=0
        r=len(m)-1
        while l<=r:
            mid=l+(r-l)//2
            if(m[mid]==target):
                return True
            elif m[mid]<target:
                l=mid+1
            elif m[mid]>target:
                r=mid-1
        return False
        