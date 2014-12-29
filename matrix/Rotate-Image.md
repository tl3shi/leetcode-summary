# Rotate Image

题目来源：[Rotate Image](https://oj.leetcode.com/problems/rotate-image/)

>
	You are given an n x n 2D matrix representing an image.
	Rotate the image by 90 degrees (clockwise).
	Follow up:
	Could you do this in-place?

解题思路：

###  常规

```cpp
	
	void rotate(vector<vector<int> > &matrix)
	{
	    int n = matrix.size();
	    for(int row = 0; row < n / 2; row++)
	    {
	        for(int col = row; col < n - row - 1; col++)
	        {
	            int top = matrix[row][col]; // back top
	            //left->top
	            matrix[row][col] = matrix[n-col-1][row];
	            //bottom->left
	            matrix[n-col-1][row] = matrix[n-row-1][n-col-1];
	            //right->bottom
	            matrix[n-row-1][n-col-1] = matrix[col][n-row-1];
	            //top->right
	            matrix[col][n-row-1] = top;
	        }
	    }
	}
```

###  高级解法

参考[discuss](https://oj.leetcode.com/discuss/3064/in-place-solution)
	
	//[discurs]
	//(1) write your matrix on a paper.
	//(2) flip (not rotate) the paper upside down. (reverse)
	//(3) flip again, but this time bottom edge to the right. (swap)
	123     789    741
	456  —> 456 —> 852 —>OK
	789     123    963
	
```cpp
	
	void rotate(vector<vector<int> > &matrix) 
    {
        int m = matrix.size(); if(m == 0) return;
        int n = matrix[0].size();
        std::reverse(matrix.begin(), matrix.end());
        for(int i = 0; i < m; i++)
            for(int j = 0; j < i; j++)
                std::swap(matrix[i][j], matrix[j][i]);
    }
```

