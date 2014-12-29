# N Queens

题目来源：[N-Queens](https://oj.leetcode.com/problems/n-queens/)

>
	The n-queens puzzle is the problem of placing n queens on an n×n chessboard such that no two queens attack each other.
	Given an integer n, return all distinct solutions to the n-queens puzzle.
	Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space respectively.
	For example,
	There exist two distinct solutions to the 4-queens puzzle:
	[
	 [".Q..",  // Solution 1
	  "...Q",
	  "Q...",
	  "..Q."],
	 ["..Q.",  // Solution 2
	  "Q...",
	  "...Q",
	  ".Q.."]
	]

解题思路：

八(N)皇后问题，经典回溯法。

```cpp
	
	vector<string> genResult(const vector<int> &queen)
    {
        int n = queen.size();
        vector<string> solution(n, string(n, '.')); 
        for(int i = 0; i < n; i++)
            solution[i][queen[i]] = 'Q';
        return move(solution);
    }
    
    bool canPut(const vector<int> &queen, int row, int col)
    {
        int n = queen.size();
        //for(int i = 0; i < n; i++) //no need, check after row
        for(int i = 0; i < row; i++)
        {
            if(queen[i] == -1) continue;
            if(queen[i] == col //|| queen[row] != -1 row one by one, no need
            || abs(i - row) == abs(queen[i] - col))
                return false;
        }
        return true;
    }
    void dfs(vector<vector<string>> &result, vector<int> &queen, int startRow)
    {
        int n = queen.size();
        if(startRow == n)
        {
            result.push_back(genResult(queen));
            return;
        }
        for(int col = 0; col < n; col++)
        {
            if(canPut(queen, startRow, col))
            {
                queen[startRow] = col;
                dfs(result, queen, startRow+1);
                queen[startRow] = -1;
            }
        }
    }
    
    vector<vector<string> > solveNQueens(int n) 
    {
        assert(n != 0);
        vector<vector<string> > result;
        vector<int> queen(n, -1);
        dfs(result, queen, 0);
        return move(result);
    }
```
 

