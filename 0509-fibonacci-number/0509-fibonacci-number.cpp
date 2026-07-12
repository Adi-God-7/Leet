class Solution {
public:
    int fib(int n) {
        int x=0;
        int y=1;
        int sum=0;
        if(n==1) sum=1;
        else{
        for(int i=0;i<n-1;i++){
            sum=x+y;
            x=y;
            y=sum;
        }
        }
    return sum;
    }
};