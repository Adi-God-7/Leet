#include <stdio.h>
#include <string.h>
#include <stdlib.h>

char* getHint(char* secret, char* guess) {
    int a = 0, b = 0;
    int n = strlen(secret);
    int cs[10] = {0}, cg[10] = {0};
    for (int i = 0; i < n; i++) {
        if (secret[i] == guess[i])
            a++;
        else {
            cs[secret[i] - '0']++;
            cg[guess[i] - '0']++;
        }
    }
    for (int i = 0; i < 10; i++)
        b += cs[i] < cg[i] ? cs[i] : cg[i];
    char* res = (char*)malloc(10 * sizeof(char));
    sprintf(res, "%dA%dB", a, b);
    return res;
}
