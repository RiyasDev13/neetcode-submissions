class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col = len(grid[0])

        def dfs(curRow,curCol):

            if (curRow < 0 or curRow >= row or curCol < 0 or curCol >= col or grid[curRow][curCol] == "0"):


                return 

            grid[curRow][curCol] = "0"
            dfs(curRow - 1 , curCol)
            dfs(curRow,      curCol + 1)
            dfs(curRow + 1 , curCol)
            dfs(curRow,      curCol - 1) 

        count = 0
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1":
                    dfs(i,j)
                    count += 1
        return count


        