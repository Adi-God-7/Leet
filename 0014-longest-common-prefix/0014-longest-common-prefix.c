char* longestCommonPrefix(char** strs, int strsSize) {
    if (strsSize == 0) return "";
    static char res[200];  
    int k = 0;
    
    for (int i = 0; strs[0][i] != '\0'; i++) {
        char c = strs[0][i];
        for (int j = 1; j < strsSize; j++) {
            if (strs[j][i] != c) {  
                res[k] = '\0';
                return res;
            }
        }
        res[k++] = c; 
    }
    
    res[k] = '\0';
    return res;
}
