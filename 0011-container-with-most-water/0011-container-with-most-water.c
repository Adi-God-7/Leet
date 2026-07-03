int maxArea(int* height, int heightSize) {
    int l=0;
    int h=heightSize-1;
    int max=0;
    int area;
    while(l<h){
        int ht = (height[l] < height[h]) ? height[l] : height[h];
        int area = ht * (h - l);
        if(height[l]<height[h]){
            l++;
        }
        else{
            h--;
        }
        if(max<area) max=area;
    }
    return max;
}