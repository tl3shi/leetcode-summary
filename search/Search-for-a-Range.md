# Search for a Range

题目来源：[Search for a Range](https://oj.leetcode.com/problems/search-for-a-range/)

>
	Given a sorted array of integers, find the starting and ending position of a given target value.
	Your algorithm's runtime complexity must be in the order of O(log n).
	If the target is not found in the array, return [-1, -1].
	For example,
	Given [5, 7, 7, 8, 8, 10] and target value 8,
	return [3, 4].

解题思路：

二分搜索,搜到了后前后找相同的,非Log(n)算法。
lower返回插入点(相等的最小的index)的位置，upper返回比target大的位置。right从n开始，非n-1；

[std::lower_bound](http://en.cppreference.com/w/cpp/algorithm/lower_bound).

[std::upper_bound](http://en.cppreference.com/w/cpp/algorithm/upper_bound).


```cpp
	
	int lower(int *A, int n, int target)
	{
	    int left = 0;
	    int right = n;
	    while(left != right)
	    {
	        int mid = left + ((right - left)>>1);
	        if(A[mid] < target)
	            left = mid+1;
	        else
	            right = mid;//NOT mid-1
	    }
	    return left;
	}
	int upper(int *A, int n, int target)
	{
	    int left = 0;
	    int right = n;
	    while(left != right)
	    {
	        int mid = left + ((right - left)>>1);
	        if(A[mid] <= target)
	            left = mid+1;
	        else
	            right = mid;//NOT mid-1
	    }
	    return left;
	}
	
	vector<int> searchRange(int A[], int n, int target)
	{
	    assert(A != NULL && n != 0);
	    int left = lower(A, n, target);
	    int right = upper(A, n, target);
	    if(left == n || A[left] != target)
	        return vector<int>(2, -1);
	    return vector<int>{left, right-1};
	
	} 
```

 

