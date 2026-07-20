class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        l=[]
        res=[]
        s=0
        for i in grid:
            l.extend(i)
        k%=len(l)
        l[:]=l[-k:]+l[:-k]
        n=len(l)/len(grid)
        for i in range(len(grid)):
            ans =l[s:s+n]  
            s+=n
            res.append(ans)
        return res

        