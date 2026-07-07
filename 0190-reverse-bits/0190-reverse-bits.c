int reverseBits(int n){
    unsigned int num=(unsigned int)n; 
    unsigned int res=0;

    for (int i=0;i<32;i++){
        res=(res<<1)|(num & 1);
        num>>=1;
    }
    return (int)res;
}