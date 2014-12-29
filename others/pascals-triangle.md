# Pascal's Triangle

题目来源：[Pascal's Triangle](https://oj.leetcode.com/problems/pascals-triangle/)

>

	Given numRows, generate the first numRows of Pascal's triangle.
	For example, given numRows = 5,
	Return
	[
	     [1],
	    [1,1],
	   [1,2,1],
	  [1,3,3,1],
	 [1,4,6,4,1]
	]
	
解题思路：

杨辉三角～

```cpp
	
	vector<vector<int> > generate(int numRows) 
    {
        vector<vector<int> > result;
        for(int i = 0; i < numRows; i++)
        {
            vector<int> row(i+1, 1);
            for(int j = 1; j < i; j++)
                row[j] = result[i-1][j-1] + result[i-1][j];
            result.push_back(row);
        }
        return move(result);
    }
```

还可以用二项式系数那个公式算。在[Pascal's Triangle II](http://tanglei.me/leetcode/pascals-triangle-ii.html)中有，这里就不再贴了。

