int max(int a,int b){
    return a>b?a:b;
}
int min(int a,int b){
    return a<b?a:b;
}

int maxProduct(int* nums,int numsSize){

    int maxProd=nums[0];
    int minProd=nums[0];
    int ans=nums[0];
    for (int i=1;i<numsSize;i++){
        if(nums[i]<0){
            int temp=maxProd;
            maxProd=minProd;
            minProd=temp;
        }
        maxProd=max(nums[i],maxProd*nums[i]);
        minProd=min(nums[i],minProd*nums[i]);
        ans=max(ans,maxProd);
    }
    return ans;
}
