class Solution {
public:
    bool checkOverlap(int radius, int xCenter, int yCenter, int x1, int y1, int x2, int y2) {
        int rs=pow(radius,2);
        for(int i=x1;i<=x2;i++){
            for(int j=y1;j<=y2;j++){
                int a=i-xCenter;
                int b=j-yCenter;
                int D=pow(a,2)+pow(b,2);
                if(D<=rs){
                    return true;
                }
            }
        }
        return false;
    }
};