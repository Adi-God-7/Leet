char* shiftingLetters(char* s, int* shifts, int shiftsSize) {
    int total = 0;
    for (int i = shiftsSize - 1; i >= 0; i--) {
        total = (total + shifts[i]) % 26;
        s[i] = ((s[i] - 'a' + total) % 26) + 'a';
    }

    return s;
}
