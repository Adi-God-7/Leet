class Solution {
public:
    int strStr(string haystack,string needle) {
        int lenneedle=needle.length();

        for(int i=0;i+lenneedle<=haystack.length();i++) {
            if(haystack.substr(i,lenneedle)==needle)
                return i;
        }
        return -1;
    }
};