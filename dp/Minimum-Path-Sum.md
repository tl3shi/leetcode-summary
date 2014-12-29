# Minimum Path Sum

题目来源：[Minimum Path Sum](https://oj.leetcode.com/problems/minimum-path-sum/)

>
	Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right which minimizes the sum of all numbers along its path.
	Note: You can only move either down or right at any point in time.

解题思路：

###  递归

用递归思路比较清晰，然后转成迭代。

```cpp

    int min(vector<vector<int> >&grid, int row, int col) 
    { 
        if(row == 0) 
        { 
            int result = 0; 
            for(int i = 0; i <= col; i++) 
                result += grid[0][i]; 
            return result; 
        } 
        if(col == 0) 
        { 
            int result = 0; 
            for(int i = 0; i <= row; i++) 
                result += grid[i][0]; 
            return result; 
        } 
        int fromleft = min(grid, row, col-1); 
        int fromup = min(grid, row-1, col); 
        return std::min(fromleft, fromup); 
    } 
```

###  动态规划, O(m+n)空间

```cpp
	
	int minPathSum(vector<vector<int> > &grid)
	{
	    int m = grid.size(); if(m == 0) return INT_MIN;
	    int n = grid[0].size();
	    vector<vector<int> > dp(m, vector<int>(n, 0));
	    dp[0][0] = grid[0][0];
	    for(int i = 1; i < n; i++)
	        dp[0][i] = dp[0][i-1] + grid[0][i];
	    for(int i = 1; i < m; i++)
	        dp[i][0] = dp[i-1][0] + grid[i][0];
	    for(int i = 1; i < m; i++)
	        for(int j = 1; j < n; j++)
	            dp[i][j] = std::min(dp[i-1][j], dp[i][j-1]) + grid[i][j];
	    return dp[m-1][n-1];
	}
```


###  动态规划, O(n)空间

更加节约点空间可以这样. 参考了[leetcode-cpp](https://github.com/soulmachine/leetcode)
	
	f[j] = min(f[j-1], f[j])+grid[i][j];
	右边的f[j]是老的f[j]表示v[i-1][j], f[j-1]即为v[i][j-1]
	左边f[j]是新的,即v[i][j].

```cpp

	int minPathSum(vector<vector<int > > &grid)
	{
		int m = grid.size();  if (m == 0) return INT_MIN;
		int n = grid[0].size();
		vector< int> f(n, INT_MAX );
		f[0] = 0;
		for (int i = 0; i < m; i++)
		{
		 	f[0] += grid[i][0];
		  	for (int j = 1; j < n; j++)
		    	f[j] = std::min(f[j - 1], f[j]) + grid[i][j];
		}
		return f[n - 1];
	}
```


