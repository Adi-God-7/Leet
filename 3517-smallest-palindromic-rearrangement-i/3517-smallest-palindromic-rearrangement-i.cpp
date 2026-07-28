class Solution {
public:
    string smallestPalindrome(string s) {
        int n=s.length();
        vector<int> bucket(26,0);
        for(int i=0;i<n/2;i++){
            bucket[s[i]-'a']++;
        }
        string l="";
        for(int i=0;i<26;i++){
            l+=string(bucket[i],'a'+i);
        }
        string m=n%2!=0?string(1,s[n/2]):"";
        string r=l;
        reverse(r.begin(),r.end());
        return l+m+r;
    }
};