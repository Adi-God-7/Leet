int maxSubArray(int* nums, int numsSize) {
    int sum=0;
    int ans=nums[0];
    for(int i=0;i<numsSize;i++){
            sum+=nums[i];
            if(sum>ans){
                ans=sum;
            }
            if(sum<0){
                sum=0;
            }
            
        }
    return ans;
}