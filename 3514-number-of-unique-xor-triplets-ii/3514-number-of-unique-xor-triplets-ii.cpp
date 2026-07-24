class Solution {
public:
    int uniqueXorTriplets(vector<int>& nums) {
        int m=0;
        for(int num:nums){
            m=max(m,num);
        }
        int u=1;
        while(u<=m){
            u<<=1;
        }
        vector<bool> one(u,false);
        vector<bool> two(u,false);
        vector<bool> three(u,false);

        for(int v:nums){
            one[v]=true;
            for(int x=0;x<u;x++){
                if(one[x]) two[x^v]=true;
            }
        }
        for(int v:nums){
            for(int x=0;x<u;x++){
                if(two[x]) three[x^v]=true;
            }
        }
        int ans=0;
        for(bool value:three){
            if(value) ans++;
        }
        return ans;
    }
};