# Trapping Rain Water

题目来源：[Trapping Rain Water](https://oj.leetcode.com/problems/trapping-rain-water/)

>
	Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.
	For example, 
	Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.

![](http://tl3shi.github.com/resource/blogimage/leetcode-rainwatertrap.png)

解题思路：

###  O(2\*n)

先找打最高的柱子, 然后从两边往中间走, 如从左到右时, maxHeight记录到当前位置最高的柱子, 若当前高度cur小于maxHeight, 则 water += maxHeight - cur;

参考了 [soulmachine 's leetcode](https://github.com/soulmachine/leetcode); 

```cpp
	
	int trap(int A[], int n) 
    {
        if(n == 0) return 0;
        int maxIndex = 0;
        for(int i = 1; i < n; i++)
            if(A[i] > A[maxIndex]) maxIndex = i;
        int lastMaxHeight = 0;
        int water = 0;
        for(int i = 0; i < maxIndex; i++)
        {
            if(A[i] > lastMaxHeight) 
                lastMaxHeight = A[i];
            else
                water += lastMaxHeight - A[i];
        }
        lastMaxHeight = 0;
        for(int i = n-1; i > maxIndex; i--)
        {
            if(A[i] > lastMaxHeight)
                lastMaxHeight = A[i];
            else
                water += lastMaxHeight - A[i];
        }
        return water;
    }
```

###  O(n)

>
	one pass and constant space,one point starts from left,another starts from right,and store the level at present,calculate the area of rectangle "all",and remove the area of block "block".It's the answer. 
	
先假设没有中间的柱子，只有最边上的两根，算出容量，然后往中间走，一个一个的加柱子，加容量，计算柱子挡住的容量，最后减去即可。	

参考 [discuss](https://oj.leetcode.com/discuss/3546/any-one-pass-solutions).

```cpp
	
	int trap(int A[], int n)
	{
	    if(n == 0) return 0;
	    int left = 0; int right = n-1;
	    int cur = 0;
	    int total = 0; int block = 0;
	    while(left <= right)
	    {
	        int tmp = std::min(A[left], A[right]);
	        if(tmp > cur)
	        {
	            total += (tmp - cur)*(right - left + 1);
	            cur = tmp;
	        }
	        if(A[left] < A[right])
	            block += A[left++];
	        else
	            block += A[right--];
	    }
	    return total - block;
	}
```

类似的题目还有 [Container With Most Water](./container-with-most-water.html).

