# Surrounded Regions

题目来源：[Surrounded Regions](https://oj.leetcode.com/problems/surrounded-regions/)

>

    Given a 2D board containing 'X' and 'O', capture all regions surrounded by 'X'.

    A region is captured by flipping all 'O's into 'X's in that surrounded region.

    For example,
    X X X X
    X O O X
    X X O X
    X O X X
    After running your function, the board should be:

    X X X X
    X X X X
    X X X X
    X O X X

解题思路：

这个题关键在与能想到跟最外面的'O'连通的就能“幸免于难”, 因此可以从从最外层的O开始往里dfs/bfs搜索，把连在一起的O记录下来(比如暂时改成另外的符号)，遍历完之后，再把所有的搜索一遍，这时仍然是’O’的就要变成’X’了，是之前暂存的，要还原成’O’. [ref](http://blog.csdn.net/shiquxinkong/article/details/18241833)

```cpp
	
	void dfs(vector<vector<char>> &board, int row, int col)
    {
        int m = board.size(); 
        assert(m >= 1);
        int n = board[0].size();
        if(row >= m || col >= n || row < 0 || col < 0)
            return;
        if(board[row][col] == 'O')
        {
            board[row][col] = '.';
            dfs(board, row-1, col); //up
            dfs(board, row+1, col); //down
            dfs(board, row, col-1); //left
            dfs(board, row, col+1); //right
        }
    }
    
    void solve(vector<vector<char>> &board) 
    {
        int m = board.size();
        if(m == 0) return; 
        int n = board[0].size();
        for(int col = 0; col < n; col++)//top and bottom
        {
            dfs(board, 0, col);
            dfs(board, m-1, col);
        }
        for(int row = 0; row < m; row++) //left and right
        {
            dfs(board, row, 0);
            dfs(board, row, n-1);
        }
        //all the 'O' the outmost has been changed to '.', 
        //now rollback and change the others 'O' -> 'X'
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
            {
                if(board[i][j] == '.')
                    board[i][j] = 'O';
                else if(board[i][j] == 'O')
                    board[i][j] = 'X';
            }
    }
```

或者将上面的dfs换成bfs也一样。

```cpp

	bool check(int row, int col, vector<vector<char> >&board)
	{
	    if(row < 0 || col < 0 || row >= board.size() || col >= board[0].size())
	        return false;
	    if(board[row][col] == 'O')
	        return true;
	    return false;
	}
	
	void bfs(vector<vector<char> >&board, int row, int col)
	{
	    queue<std::pair<int, int> > coords;
	    coords.push(std::pair<int, int>(row, col));
	    while(coords.size() > 0)
	    {
	        int r = coords.front().first;
	        int c = coords.front().second;
	        coords.pop();
	        if(check(r, c, board))
	        {
	            board[r][c] = '.';//mark
	            if(check(r-1, c, board))//or check later (the up 'if')
	                coords.push(std::pair<int,int>(r-1, c));
	            if(check(r+1, c, board))
	                coords.push(std::pair<int,int>(r+1, c));
	            if(check(r, c-1, board))
	                coords.push(std::pair<int,int>(r, c-1));
	            if(check(r, c+1, board))
	                coords.push(std::pair<int,int>(r, c+1));
	        }
	    }
	}
```

