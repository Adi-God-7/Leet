void gameOfLife(int** board, int boardSize, int* boardColSize) {
    int m = boardSize;
    int n = boardColSize[0];
    int dir[8][2] = {{1,0},{-1,0},{0,1},{0,-1},{1,1},{1,-1},{-1,1},{-1,-1}};
    
    int f[m][n];
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            f[i][j] = board[i][j];
        }
    }
    
    for (int i = 0; i < m; i++) {
        for (int j = 0; j < n; j++) {
            int ln = 0;
            
            for (int d = 0; d < 8; d++) {
                int r = i + dir[d][0];
                int c = j + dir[d][1];
                if (r >= 0 && r < m && c >= 0 && c < n && f[r][c] == 1)
                    ln++;
            }
            
            if (f[i][j] == 1 && (ln < 2 || ln > 3))
                board[i][j] = 0; 
            else if (f[i][j] == 0 && ln == 3)
                board[i][j] = 1;
        }
    }
}
