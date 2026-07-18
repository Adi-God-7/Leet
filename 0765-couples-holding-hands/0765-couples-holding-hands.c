int minSwapsCouples(int* row, int rowSize) {
    int count = 0;
    for (int i = 0; i < rowSize; i += 2) {
        int partner = row[i]^1; 
        if (row[i + 1] != partner) {
            for (int j = i + 2; j < rowSize; j++) {
                if (row[j] == partner) {
                    int temp = row[j];
                    row[j] = row[i + 1];
                    row[i + 1] = temp;
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}
