int maxProfit(int* prices, int n) {
    int bp = prices[0];
    int pro = 0;

    for(int i = 1; i < n; i++) {
        if(prices[i] < bp) {
            bp = prices[i];   
        } 
        else {
            int profit = prices[i] - bp;
            if(profit > pro)
                pro = profit; 
        }
    }
    return pro;
}
