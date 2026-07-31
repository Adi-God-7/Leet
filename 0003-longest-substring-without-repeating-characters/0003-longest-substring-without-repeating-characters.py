class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        seen={}
        start=0
        ml=0
        
        for end, char in enumerate(s):
            
            if char in seen and seen[char] >= start:
                start=seen[char]+1
            
           
            seen[char] = end
            
            cl=end-start+1
            if cl > ml:
                ml = cl
            
        return ml