# Spiral Matrix II

题目来源：[Spiral Matrix II](https://oj.leetcode.com/problems/spiral-matrix-ii/)

>
	Given an integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.	
	For example,
	Given n = 3,
	You should return the following matrix:
	[
	 [ 1, 2, 3 ],
	 [ 8, 9, 4 ],
	 [ 7, 6, 5 ]
	]

解题思路：

跟 [spiral-matrix](./spiral-matrix.html)一样。

```cpp
	
	vector<vector<int> > generateMatrix(int n)
	{
	    if(n == 0) return vector<vector<int> >();
	    vector<vector<int> > matrix(n, vector<int>(n, 0));
	    int rowindex = 0;
	    int columeindex = n-1;
	    int row = n, colume = n;
	    int index = 1;
	    int size = n * n;
	    while(true)
	    {
	        int toleft_start = rowindex;
	        int toleft_end = columeindex;
	        int todown_start = rowindex + 1;
	        int todown_end = row - rowindex - 1;
	        
	        for(int i = toleft_start; i <= toleft_end; i++)
	            matrix[rowindex][i] = index++;
	        if(index == size+1)
	            break;
	        for(int i = todown_start; i <= todown_end; i++)
	            matrix[i][columeindex] = index++;
	        if(index == size+1)
	            break;
	        for(int i = toleft_end-1; i>= toleft_start; i--)
	            matrix[row - rowindex - 1][i] = index++;
	        if(index == size+1)
	            break;
	        for(int i = todown_end-1; i >= todown_start; i--)
	            matrix[i][colume-columeindex-1] = index++;
	        if(index == size+1)
	            break;
	        rowindex++;
	        columeindex--;
	    }
	    return move(matrix);
	}
```

 
 

