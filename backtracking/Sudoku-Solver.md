# Sudoku Solver

题目来源：[Sudoku Solver](https://oj.leetcode.com/problems/sudoku-solver/)

>
	Write a program to solve a Sudoku puzzle by filling the empty cells.
	Empty cells are indicated by the character '.'.
	You may assume that there will be only one unique solution.

解题思路：

记录需要填充的每个位置，然后用1-9一个一个去试～ 深搜即可。 类似的问题还有[八皇后](./n-queens.html)等。

```cpp
	
	//check if can put x in board[row][col]
    bool canPut(vector<vector<char> > &board, int row, int col, char x)
    {
        for(int i = 0; i < 9; i++)
        {
            if(board[i][col] == x) return false;
            if(board[row][i] == x) return false;
            int r = 3 * (row / 3) + i / 3;
            int c = 3 * (col / 3) + i % 3;
            if(board[r][c] == x) return false;
        }
        return true;
    } 
    bool search(vector<vector<char> > &board, const vector<std::pair<int, int>> &need, int start)
    {
        if(start == need.size())
            return true;
        int r = need[start].first;
        int c = need[start].second;
        for(char x = '1'; x <= '9'; x++)
        {
            if(canPut(board, r, c, x))
            {
                board[r][c] = x;
                if(search(board, need, start+1))
                    return true;
                board[r][c] = '.'; //rollback
            }
        }
    }
    void solveSudoku(vector<vector<char> > &board) 
    {
        vector<std::pair<int, int>> need;
        for(int i = 0; i < 9; i++)
            for(int j = 0; j < 9; j++)
                if(board[i][j] == '.')
                    need.push_back(make_pair(i, j));
        search(board, need, 0);
    }
```
 

