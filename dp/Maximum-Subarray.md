# Maximum Subarray

题目来源：[Maximum Subarray](https://oj.leetcode.com/problems/maximum-subarray/)

>
	Find the contiguous subarray within an array (containing at least one number) which has the largest sum.
	For example, given the array [−2,1,−3,4,−1,2,1,−5,4],
	the contiguous subarray [4,−1,2,1] has the largest sum = 6.
	More practice:
	If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

解题思路：

注意此例是连续subarray,且最少得选1个。

若当前i，前面i-1的结果若为负的话，新序列就从当前A[i]开始算起了，不然就将当前A[i]附加上去。

###  DP, O(n) 空间

```cpp
	
	int maxSubArray(int A[], int n) 
    {
        assert(n != 0);
        vector<int> dp(n, 0);
        dp[0] = A[0];
        int result = A[0];
        for(int i = 1; i < n; i++)
        {
            if(dp[i-1] < 0)
                dp[i] = A[i];
            else
                dp[i] = dp[i-1] + A[i];
            result = std::max(result, dp[i]);
        }
        return result;
    }
```

###  DP, O(1) 空间

上面的优化一下即可。

```cpp
	
	//Kadane's algorithm O(n)
    //max_end_here是结束位置为i-1的最大子数组和
    int maxSubArray(int A[], int n)
    {
        int max_so_far = A[0];
        int max_end_here = A[0];
        for(int i = 1; i < n; i++)
        {
            if(max_end_here < 0)
                max_end_here = A[i];
            else
                max_end_here += A[i];
            max_so_far = std::max(max_so_far, max_end_here);
        }
        return max_so_far ;
    }
```


###  分治, O(nlogn)

分治算法：要么左半/右半，要么包括中间的和左右两边都有部分, 时间复杂度```O(NlogN)```.

```cpp

	//Divide and Conquer O(nlogn)
    int maxSubArrayDAC(int A[], int left, int right)
    {
        if(right < left) return INT_MIN;
        if(right == left)
            return A [left]; //at least 1 element
        int mid = left + ((right - left)>>1);
        //across left and right
        int crossSumLeft = A[mid]; //including mid
        int crossMaxLeft = A[mid];
        for(int i = mid-1; i >= left; i--)
        {
            crossSumLeft += A[i];
            crossMaxLeft = std::max(crossMaxLeft, crossSumLeft);
        }
        int crossSumRight = A[mid];
        int crossMaxRight = A[mid];
        for(int i = mid+1; i <= right; i++)
        {
            crossSumRight += A[i];
            crossMaxRight = std::max(crossMaxRight, crossSumRight);
        }
        int crossMax = crossMaxLeft + crossMaxRight - A[mid];
        int leftMax = maxSubArrayDAC( A, left , mid-1);
        int rightMax = maxSubArrayDAC( A, mid+1, right );
        return std::max(std::max(leftMax, rightMax), crossMax);
    } 
    int maxSubArray(int A[], int n)
    {
        assert(n != 0);
        if(n == 1) return A[0];
        return maxSubArrayDAC(A, 0, n-1) ;
    }
```

参考资料:

- [ref](http://en.wikipedia.org/wiki/Maximum_subarray_problem)

