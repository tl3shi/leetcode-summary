# Unique Paths II

题目来源：[Unique Paths II](https://oj.leetcode.com/problems/unique-paths-ii/)

>
    Follow up for "Unique Paths":
    Now consider if some obstacles are added to the grids. How many unique paths would there be?
    An obstacle and empty space is marked as 1 and 0 respectively in the grid.
    For example,
    There is one obstacle in the middle of a 3x3 grid as illustrated below.
    [
      [0,0,0],
      [0,1,0],
      [0,0,0]
    ]
    The total number of unique paths is 2.
    Note: m and n will be at most 100.

解题思路：
跟 [minimum-path-sum](./minimum-path-sum.html)差不多. 
这里就省却递归方法了，直接用DP。

```cpp
    
    int uniquePathsWithObstacles(vector<vector<int> > &grid) 
    {
        int m = grid.size(); if (m == 0) return 0;
        int n = grid[0].size();
        if(grid[0][0] == 1) return 0;
        vector<vector<int> > dp(m, vector<int>(n, 0));
        for(int i = 0; i < n; i++)
        {
            if(grid[0][i] == 1)
                break;
            dp[0][i] = 1;
        }
        for(int i = 0; i < m; i++)
        {
            if(grid[i][0] == 1)
                break;
            dp[i][0] = 1;
        }
        for(int i = 1; i < m; i++)
            for(int j = 1; j < n; j++)
            {
                if(grid[i][j] == 1)
                    dp[i][j] = 0;
                else
                    dp[i][j] = dp[i-1][j] + dp[i][j-1];
           }
        return dp[m-1][n-1];
    }
    
```


