bool isAnagram(char* s, char* t) {
    int freq[26]={0};
    int i=0;
    while(s[i]!='\0'){
        freq[s[i]-'a']++;
        i++;
    }
    i=0;
    while(t[i]!='\0'){
        freq[t[i]-'a']--;
        i++;
    }
    for(i=0;i<26;i++){
        if(freq[i]!=0)
            return false;
    }
    return true;
}
