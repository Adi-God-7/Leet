class Solution {
public:
    bool checkDivisibility(int n) {
        int s=0;
        int p=1;
        int t=n;
        while(t!=0){
            int r=t%10;
            t/=10;
            s+=r;
            p*=r;
        }
        if(n%(s+p)==0) return true;
        return false;
    }
};