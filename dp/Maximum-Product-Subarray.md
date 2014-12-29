# Maximum Product Subarray

题目来源：[Maximum Product Subarray](https://oj.leetcode.com/problems/maximum-product-subarray/)

>
	Find the contiguous subarray within an array (containing at least one number) which has the largest product.	
	For example, given the array [2,3,-2,4],
	the contiguous subarray [2,3] has the largest product = 6.

解题思路：

###  暴力O(n^2)

超时

```cpp
	
	int maxProductN2(int A[], int n)
	{
	    assert(A != NULL && n != 0);
	    if (n == 1) return A[0];
	    int result = A[0];
	    for(int i = 0; i < n; i++)
	    {
	        int t = 1;
	        for(int j = i; j >= 0; j--)
	        {
	            t *= A[j];
	            result = std::max(result, t);
	        }
	    }
	    return result;
	}
```

###  DP O(n)

记录到i为止的最大值和最小值，最小值乘以当前值可能反而变成最大值，不用去考虑当前A[i]的值的正负，分情况讨论，这样反而复杂。

```cpp
	
	int maxProduct(int A[], int n)
	{
	    assert(A != NULL && n != 0);
	    if (n == 1) return A[0];
	    int result = A[0];
	    vector<int> dpMin(n, 0);
	    vector<int> dpMax(n, 0);
	    dpMax[0] = dpMin[0] = A[0];
	    for(int i = 1; i < n; i++)
	    {
	        dpMax[i] = std::max(std::max(dpMax[i-1]*A[i], dpMin[i-1]*A[i]), A[i]);
	        result = std::max(result, dpMax[i]);
	        dpMin[i] = std::min(std::min(dpMin[i-1]*A[i], dpMax[i-1]*A[i]), A[i]);
	    }
	    return result;
	}
```

可以用O(1)的空间，记录上一次的结果。代码就直接贴 [discuss](https://oj.leetcode.com/discuss/11923/sharing-my-solution-o-1-space-o-n-running-time) 里的了。

```cpp

	//[ref](https://oj.leetcode.com/discuss/11923/sharing-my-solution-o-1-space-o-n-running-time)
	int maxProduct(int A[], int n)
	{
	    assert(A != NULL && n != 0);
	    int maxherepre = A[0];
	    int minherepre = A[0];
	    int maxsofar = A[0];
	    int maxhere = 0; int minhere = 0;
	
	    for (int i = 1; i < n; i++) {
	        maxhere = std::max(std::max(maxherepre * A[i], minherepre * A[i]), A[i]);
	        minhere = std::min(std::min(maxherepre * A[i], minherepre * A[i]), A[i]);
	        maxsofar = std::max(maxhere, maxsofar);
	        maxherepre = maxhere;
	        minherepre = minhere;
	    }
	    return maxsofar;
	}
```

