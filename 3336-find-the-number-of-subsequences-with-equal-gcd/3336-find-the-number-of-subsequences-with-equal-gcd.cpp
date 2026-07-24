class Solution {
public:
    static const int MOD = 1e9 + 7;

    int subsequencePairCount(vector<int>& nums) {

        const int MAXG = 200;

        vector<vector<long long>> dp(
            MAXG + 1,
            vector<long long>(MAXG + 1, 0)
        );

        dp[0][0] = 1;

        for (int x : nums) {

            vector<vector<long long>> next = dp;

            for (int g1 = 0; g1 <= MAXG; g1++) {

                for (int g2 = 0; g2 <= MAXG; g2++) {

                    long long ways = dp[g1][g2];

                    if (ways == 0) {
                        continue;
                    }

                    int newG1 = gcd(g1, x);
                    int newG2 = gcd(g2, x);

                    next[newG1][g2] =
                        (next[newG1][g2] + ways) % MOD;

                    next[g1][newG2] =
                        (next[g1][newG2] + ways) % MOD;
                }
            }

            dp = move(next);
        }

        long long answer = 0;

        for (int g = 1; g <= MAXG; g++) {
            answer = (answer + dp[g][g]) % MOD;
        }

        return answer;
    }
};