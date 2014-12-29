# Triangle

题目来源：[Triangle](https://oj.leetcode.com/problems/triangle/)

>

    Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.
    For example, given the following triangle
    [
         [2],
        [3,4],
       [6,5,7],
      [4,1,8,3]
    ]
    The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).
    Note:
    Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.


解题思路：

动态规划，从下往上走～ 
`rows[col] = std::min(rows[col], rows[col+1]) + triangle[row][col];`

```cpp
    
    int minimumTotal(vector < vector< int > > &triangle )
    {
        int m = triangle .size();
        if (m == 0) return 0;
        vector< int > dp(triangle [m-1]);
        for( int r = m-2; r >= 0; r--) //triangle, if m is 1, dp[0] is result
            for (int c = 0; c <= r; c++) //triangle[r].size() = r+1
                dp[c] = std::min(dp[c], dp[c+1]) + triangle [r][c];
        return dp[0];
    }
```

如果triangle值可以改变的话，可以O(1)的空间复杂度。

```cpp

    //triangle can be changed
    int minimumTotal(vector < vector< int > > &triangle )
    {
        int m = triangle .size();
        if (m == 0) return 0;
        for( int r = m-2; r >= 0; r--) //triangle, if m is 1, dp[0] is result
            for (int c = 0; c <= r; c++) //triangle[r].size() = r+1
                triangle [r][c] += std::min(triangle [r+1][c], triangle[r+1][c+1]);
        return triangle [0][0];
}
```



