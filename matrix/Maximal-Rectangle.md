# Maximal Rectangle

题目来源：[Maximal Rectangle](https://oj.leetcode.com/problems/maximal-rectangle/)

>
	Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing all ones and return its area.

解题思路：

### O(n^3) 算法

一种直接的方法是: 横向记录从左到i, 包括i为1的连续1的长度，然后再纵向去查找以这个连续1长度作为min宽的最大的高度,得到面积。O(n^3)

```cpp
	
	int getMaxHeight(const vector<vector<int> > &ones, int row, int col)
    {
        int minWidth = ones[row][col];
        int height = 0;
        for(int i = row; i >= 0; i--) //up
        {
            if(ones[i][col] >= minWidth)
                ++height;
            else 
                break;
        }
        for(int i = row+1; i < ones.size(); i++)
        {
            if(ones[i][col] >= minWidth)
                ++height;
            else
                break;
        }
        return height;
    }
    int maximalRectangle(vector<vector<char> > &matrix) 
    {
        int m = matrix.size(); if(m == 0) return 0;
        int n = matrix[0].size();
        vector<vector<int> > ones(m, vector<int>(n, 0));//[i][j], 第i行从左到j, 包括j连续1的长度
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
            {
                if(j == 0) ones[i][0] = matrix[i][j] == '1' ? 1 : 0;
                else ones[i][j] = matrix[i][j] == '1' ? ones[i][j-1]+1 : 0;
            }
        int result = 0;
        for(int i = 0; i < m; i++)
            for(int j = 0; j < n; j++)
            {
                if(ones[i][j] > 0)
                    result = std::max(result, ones[i][j] * getMaxHeight(ones, i, j));
            }
        return result;
    }
```

###  O(n^2)算法

一行一行处理，每一行，按照柱状图那道题目 [Largest Rectangle in Histogram](./Largest-Rectangle-in-Histogram.html) `O(n)`算法处理，总体复杂度O(n^2).

用栈维护了一个递增(非递减)的序列，当当前索引的元素比栈顶小时，取栈顶元素（并出栈），并将这个元素的高度和当前索引端(快降低了)构成的矩形面积，栈中上升的那段都可以出栈并计算。

```cpp
	
	int largestRectangleArea(const vector<int> &height)
    {
        int result = 0;
        stack<int> index;
        for(int i = 0; i < height.size(); i++)
        {
            if(index.empty() || height[index.top()] <= height[i] )
                index.push(i);
            else
            {
                while(!index.empty() && height[index.top()] >= height[i])
                {
                    auto t = index.top();
                    index.pop();
                    result = std::max(result, height[t] * (index.empty() ? i : (i-1)-index.top()));
                }
                index.push(i);//Do not forget.
            }
        }
        return result;
    }
    
    int maximalRectangle(vector<vector<char> > &matrix) 
    {
        int m = matrix.size(); if(m == 0) return 0;
        int n = matrix[0].size();
        vector<vector<int> > ones(m, vector<int>(n, 0));
        int result = 0;
        for(int i = 0; i < m; i++)
        {
            for(int j = 0; j < n; j++)
            {
                if(i == 0) ones[0][j] = matrix[i][j] == '1' ? 1 : 0;
                else ones[i][j] = matrix[i][j] == '1' ? ones[i-1][j]+1 : 0;
            }
            ones[i].push_back(-1);
            result = std::max(result, largestRectangleArea(ones[i]));
        }
        return result;
    }
```

以高度`[2,5,3,4,1]`为例, 2[index=0], 5[index=2]进栈, 当前高度为3, 以5为最矮的计算面积为5,然后5出栈, 此时**把3[index=2]进栈** (注意对比下[Largest Rectangle in Histogram](./Largest-Rectangle-in-Histogram.html)的写法), 一直到index=4时，1最小了, 依次计算面积, 
	
	[0,2,3,]-->[0,2,]
	4*(4-1-2)=8.
	[0,2] --> [0]
	3*(4-1-0)=9. !!max
	[0] -->[]
	2*(4)=8.

上面代码还可以优化下内存空间, 用`O(n)`n为列数量。

```cpp

	int maximalRectangle2(vector <string > & matrix)
	{
	    int m = matrix.size(); if (m == 0) return 0;
	    int n = matrix[0].size(); if (n == 0) return 0;
	    vector< int> height(n+1, 0);
	    int maxArea = 0;
	    for(int row = 0; row < m; row++)
	    {
	        for(int col = 0; col < n; col++)
	        {
	            if(matrix [row][col] == '1')
	                height[col] += 1;
	            else
	                height[col] = 0;
	        }
	        height[n] = -1; //dummy one
	        maxArea = std::max(maxArea, largestRectangleArea(height));
	    }
	    return maxArea;
	}
```


###  O(n^2)算法 思路2

参考了[leetcode-cpp](https://github.com/soulmachine/leetcode)。 思路是对当前高度h, 找左边比他小的最大的index,设为i, 右边比h小最小的index,设为j,则以h为最小高度的面积应该为 
`(j-i-1)*h`.  eg : [2,5,3,4,1], 当前高度3, 则, left=0, right = 4, area = 3*(4-0-1)=9.

```cpp

	int maximalRectangle(vector<vector<char> > &matrix) 
    {
        int m = matrix.size(); if(m == 0) return 0;
        int n = matrix[0].size();
        int result = 0;
        vector<int> leftMax(n, -1);
        vector<int> rightMin(n, n);
        vector<int> height(n, 0);
        for(int i = 0; i < m; i++)
        {
            int left = -1, right = n;
            for(int j = 0; j < n; j++)
            {
                if(matrix[i][j] == '1'){
                    ++height[j];
                    leftMax[j] = std::max(leftMax[j], left);
                }else{
                    left = j;
                    height[j]=0; leftMax[j]=-1; rightMin[j]=n;
                }
            }
            for(int j = n-1; j >= 0; j--)
            {
                 if(matrix[i][j] == '1'){
                     rightMin[j] = std::min(rightMin[j], right);
                     result = std::max(result, height[j]*(rightMin[j]-leftMax[j]-1));
                 }else{
                     right = j;
                 }
            }
        }
        return result;
    }
```


