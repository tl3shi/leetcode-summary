# N Queens II

题目来源：[N-Queens II](https://oj.leetcode.com/problems/n-queens-ii/)

>
	Follow up for N-Queens problem.
	Now, instead outputting board configurations, return the total number of distinct solutions.

解题思路：

跟上一题 [n-queens](./n-queens.html)一模一样。

```cpp
	
	bool canPut(const vector<int> &queen, int row, int col)
    {
        int n = queen.size();
        for(int i = 0; i < n; i++)
        {
            if(queen[i] == -1) continue;
            if(queen[i] == col //|| queen[row] != -1 row one by one, no need
            || abs(i - row) == abs(queen[i] - col))
                return false;
        }
        return true;
    }
    void dfs(int &result, vector<int> &queen, int startRow)
    {
        int n = queen.size();
        if(startRow == n)
        {
            ++result;
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
    
    int totalNQueens(int n) 
    {
        assert(n != 0);
        int result = 0;
         vector<int> queen(n, -1);
        dfs(result, queen, 0);
        return result;
    }
```

 

