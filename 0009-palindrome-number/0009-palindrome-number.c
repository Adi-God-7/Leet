bool isPalindrome(int x) {
    if(x<0) return false;
    bool f;
    long long og,rn=0;
    og=x;
    while(x!=0){
        int r=x%10;
        rn=rn*10+r;
        x/=10;
    }
    if(og==rn) f=true;
    else f=false;
    return f;
}