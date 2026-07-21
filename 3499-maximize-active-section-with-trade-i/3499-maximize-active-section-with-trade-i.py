class Solution:
    def maxActiveSectionsAfterTrade(self,s:str)->int:
        ones=s.count('1')
        s='1'+s+'1'

        zero=[len(x) for x in s.split('1') if x]

        if len(zero)<2:
            return ones

        best=max(zero[i]+zero[i+1] for i in range(len(zero)-1))

        return ones+best