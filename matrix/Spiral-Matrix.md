# Spiral Matrix

题目来源：[Spiral Matrix](https://oj.leetcode.com/problems/spiral-matrix/)

>
	Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.	
	For example,
	Given the following matrix:
	[
	 [ 1, 2, 3 ],
	 [ 4, 5, 6 ],
	 [ 7, 8, 9 ]
	]
	You should return [1,2,3,6,9,8,7,4,5].

解题思路：

暴力模拟～ 

```cpp
	
	vector<int> spiralOrder(vector<vector<int> > &matrix)
	{
	    vector<int> result;
	    int row = matrix.size();
	    if(row == 0) return result;
	    int colume = matrix[0].size();
	    int size = row * colume;
	    int rowindex = 0;
	    int columeindex = colume-1;
	    while(true)
	    {
	        int toleft_start = rowindex;
	        int toleft_end = columeindex;
	        int todown_start = rowindex + 1;
	        int todown_end = row - rowindex - 1;
	        
	        for(int i = toleft_start; i <= toleft_end; i++)
	            result.push_back(matrix[rowindex][i]);
	        if(result.size() == size)
	            break;
	        for(int i = todown_start; i <= todown_end; i++)
	            result.push_back(matrix[i][columeindex]);
	        if(result.size() == size)
	            break;
	        for(int i = toleft_end-1; i>= toleft_start; i--)
	            result.push_back(matrix[row - rowindex - 1][i]);
	        if(result.size() == size)
	            break;
	        for(int i = todown_end-1; i >= todown_start; i--)
	            result.push_back(matrix[i][colume-columeindex-1]);
	        if(result.size() == size)
	            break;
	        rowindex++;
	        columeindex--;
	    }
	    return move(result);
	}
```

 

