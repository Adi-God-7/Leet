class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int x1=0;
        int x2=0;
        for(int i:nums){
            x1^=i;
        }
        for(int i=0;i<=nums.size();i++){
            x2^=i;
        }
        return x1^x2;
    }
};