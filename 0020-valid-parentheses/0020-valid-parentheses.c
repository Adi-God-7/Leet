#include <stdbool.h>

bool isValid(char* s) {
    int n = strlen(s);
    char stack[n]; 
    int top = -1; 

    for (int i = 0; i < n; i++) {
        char c = s[i];
        if (c == '(' || c == '{' || c == '[') {
            stack[++top] = c; 
        } else {
            if (top == -1) return false; 
            if ((c == ')' && stack[top] != '(') ||
                (c == '}' && stack[top] != '{') ||
                (c == ']' && stack[top] != '[')) {
                return false; 
            }
            top--; 
        }
    }

    return top == -1; 
}
