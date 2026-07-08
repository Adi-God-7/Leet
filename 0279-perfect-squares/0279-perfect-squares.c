int numSquares(int n) {
    int r = (int)sqrt(n);
    if (r * r == n) return 1;

    for (int i = 1; i * i <= n; i++) {
        int rem = n - i * i;
        int s = (int)sqrt(rem);
        if (s * s == rem) return 2;
    }
    
    while (n % 4 == 0) n /= 4;
    if (n % 8 == 7) return 4;

    return 3;
}
