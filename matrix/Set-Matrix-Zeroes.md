# Set Matrix Zeroes

题目来源：[Set Matrix Zeroes](https://oj.leetcode.com/problems/set-matrix-zeroes/)

>
	Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in place.
	click to show follow up.
	Follow up:
	Did you use extra space?
	A straight forward solution using O(mn) space is probably a bad idea.
	A simple improvement uses O(m + n) space, but still not the best solution.
	Could you devise a constant space solution?

解题思路：

###   O(m + n) 空间

另用数组记录哪些行/列有0.

```cpp
	
	void setZeroes(vector<vector<int> > &matrix) 
    {
        int m = matrix.size();
        if(m == 0) return;
        int n = matrix[0].size();
        vector<bool> row(m, false);
        vector<bool> col(n, false);
        for(int i = 0; i < m; i++)
            for(int j = 0;j < n; j++)
            {
                if(matrix[i][j] == 0)
                    row[i] = col[j] = true;
            }
        for(int i = 0; i < m; i++)
            for(int j = 0;j < n; j++)
            {
                if(row[i] || col[j])
                    matrix[i][j] = 0;
            }
    }	
```

###   常数空间

假设第i行j列是0，那么第0行的j列、第0列第i行 肯定要设置为0。 所以可以用两个变量记录下第0行0列是否有，然后把其他行列的信息往这写。

```cpp
	
	 void setZeroes(vector<vector<int> > &matrix) 
    {
        int m = matrix.size();
        if(m == 0) return;
        int n = matrix[0].size();
        bool firstRow = false;
        bool firstCol = false;
        for(int i = 0; i < n; i++)
        {
            if(matrix[0][i] == 0)
            {
                firstRow = true;
                break;
            }
        }
        for(int i = 0; i < m; i++)
        {
            if(matrix[i][0] == 0)
            {
                firstCol = true; 
                break;
            }
        }
                
        for(int i = 1; i < m; i++)
            for(int j = 1;j < n; j++)
            {
                if(matrix[i][j] == 0)
                    matrix[i][0] = matrix[0][j] = 0;
            }
        for(int i = 1; i < m; i++)
            for(int j = 1;j < n; j++)
            {
                if(matrix[i][0] == 0 || matrix[0][j] == 0)
                    matrix[i][j] = 0;
            }
         if(firstRow)
         { 
             for(int i = 0; i < n; i++)
                matrix[0][i]=0;
         }
         if(firstCol)
         {
             for(int i = 0; i < m; i++)
                matrix[i][0]=0;
         }
    }
```

