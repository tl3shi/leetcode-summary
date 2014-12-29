# Search in Rotated Sorted Array

题目来源：[Search in Rotated Sorted Array](https://oj.leetcode.com/problems/search-in-rotated-sorted-array/)

>
	Suppose a sorted array is rotated at some pivot unknown to you beforehand.
	(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
	You are given a target value to search. If found in the array return its index, otherwise return -1.
	You may assume no duplicate exists in the array.

解题思路：

rotate总是至少有一半是有序的，可以根据这一半有序的值去二分。

```cpp
	
	int search(int A[], int n, int target)
	{
	    assert(n != 0);
	    int left = 0; int right = n-1;
	    while(left <= right)
	    {
	        int mid = left + ((right - left)>>1);
	        if(A[mid] == target) return mid;
	        if(A[left] <= A[mid])//left is sorted, left may equal mid
	        {
	            if(target >= A[left] && target < A[mid])//target in A[left,mid]
	                right = mid - 1;
	            else
	                left = mid + 1;
	        }else //right is sorted
	        {
	            if(target > A[mid] && target <= A[right]) //target in A[mid,right]
	                left = mid + 1;
	            else
	                right = mid - 1;
	        }
	    }
	    return -1;
	}
```

