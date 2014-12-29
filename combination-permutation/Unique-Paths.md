# Unique Paths

题目来源：[Unique Paths](https://oj.leetcode.com/problems/unique-paths/)

>
	A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
	The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
![](http://tl3shi.github.com/resource/blogimage/leetcode-unique-path.png)
>
	How many possible unique paths are there?
	Above is a 3 x 7 grid. How many possible unique paths are there?
	Note: m and n will be at most 100.

解题思路：

一共m-1+n-1步，其中任意选择m-1作为竖着走即可。
 
```cpp
	
	//C_n ^m 
    int C(int n, int m)
    {
        if(m == 0) return 1;
        if(n-m < m) return C(n, n-m);
        int i = 1;
        long long result = 1;
        while(i <= m)
        {
            result *= n-(i-1);
            result /= i;
            i++;
        }
        return (int)result;
    }
    
    int uniquePaths(int m, int n) 
    {
        return C(m-1 + n-1, m-1);
    }
```

 

