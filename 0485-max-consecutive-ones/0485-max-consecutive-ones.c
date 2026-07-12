int findMaxConsecutiveOnes(int* nums, int numsSize) {
    int maxCount = 0;
    int current = 0;

    for (int i = 0; i < numsSize; i++) {
        current = (nums[i] == 1) ? current + 1 : 0;
        maxCount = (current > maxCount) ? current : maxCount;
    }

    return maxCount;
}
