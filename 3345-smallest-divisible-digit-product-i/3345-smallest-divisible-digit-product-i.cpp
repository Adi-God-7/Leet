class Solution {
public:
    int dig(int num){
        int p=1;
        while(num!=0){
            int r=num%10;
            num/=10;
            p*=r;
        }
        return p;
    }
    int smallestNumber(int n, int t) {
        int pro=dig(n);
        while(pro%t!=0){
            n=n+1;
            pro=dig(n);
        }
        return n;
    }
};