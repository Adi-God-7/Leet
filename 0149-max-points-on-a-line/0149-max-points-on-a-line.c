#include <math.h>
#include <float.h>

int maxPoints(int** points, int pointsSize, int* pointsColSize) {
    if (pointsSize <= 2) return pointsSize;

    int max = 0;
    double a[10000]; 

    for (int i = 0; i < pointsSize; i++) {
        int count = 0, duplicate = 0, vertical = 0;
        for (int j = 0; j < pointsSize; j++) {
            if (i == j) continue;

            int dx = points[j][0] - points[i][0];
            int dy = points[j][1] - points[i][1];

            if (dx == 0 && dy == 0) {
                duplicate++;
            } 
            else if (dx == 0) {
                a[count++] = INFINITY; 
            }
             else {
                a[count++] = (double)dy / (double)dx;
            }
        }

        int Max = 1; 
        for (int m = 0; m < count; m++) {
            int sameSlope = 2; 
            for (int n = m + 1; n < count; n++) {
                if ((isinf(a[m]) && isinf(a[n])) ||
                    fabs(a[m] - a[n]) < 1e-9) {
                    sameSlope++;
                }
            }
            if (sameSlope > Max)
                Max = sameSlope;
        }
        Max += duplicate;
        if (Max > max)
            max = Max;
    }
    return max;
}
