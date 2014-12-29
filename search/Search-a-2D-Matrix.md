# Search a 2D Matrix

题目来源：[Search a 2D Matrix](https://oj.leetcode.com/problems/search-a-2d-matrix/)

>
	Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:
	Integers in each row are sorted from left to right.
	The first integer of each row is greater than the last integer of the previous row.
	For example,
	Consider the following matrix:
	[
	  [1,   3,  5,  7],
	  [10, 11, 16, 20],
	  [23, 30, 34, 50]
	]
	Given target = 3, return true.

解题思路：	
二分查找，将index转化为matrix的row/col即可。 
 
```cpp

	int cmp(vector<vector<int > > &matrix, const int m, const int n, int index, int target)
	{
	    int row = index / n;
	    int col = index % n;
	    if(matrix[row][col] == target)
	        return 0;
	    if(matrix[row][col] < target)
	        return -1;
	    return 1;
	}
	
	bool searchMatrix(vector<vector< int> > &matrix, int target)
	{
	    if(matrix.size() == 0) return false ;
	    int m = matrix.size();
	    int n = matrix[0].size();
	    int left = 0; int right = m * n - 1;
	    while(left <= right)
	    {
	        int mid = left + ((right - left)>>1);
	        int c = cmp(matrix, m, n, mid, target);
	        if (c == 0)
	            return true ;
	        else if (c < 0)
	            left = mid+1;
	        else
	            right = mid-1;
	    }
	    return false ;
	}

```

 

