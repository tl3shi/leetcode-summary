# Search in Rotated Sorted Array II

题目来源：[Search in Rotated Sorted Array II](https://oj.leetcode.com/problems/search-in-rotated-sorted-array-ii/)

>
	Follow up for "Search in Rotated Sorted Array":
	What if duplicates are allowed?	
	Would this affect the run-time complexity? How and why?
	Write a function to determine if a given target is in the array.
	
解题思路：
跟[Search in Rotated Sorted Array](./search-in-rotated-sorted-array.html)相比， 不能通过A[left] <= A[mid] 判断这段有序。

```cpp
	
	bool search(int A[], int n, int target) 
    {
        assert(n != 0);
        int left = 0; int right = n - 1;
        while(left <= right)
        {
            int mid = left + ((right-left)>>1);
            if(A[mid] == target) return true;
            if(A[left] < A[mid])//left is sorted
            {
                if(A[left] <= target && target < A[mid])
                    right = mid-1;
                else
                    left = mid+1;
            }else if(A[mid] < A[right])//right is sorted
            {
                if(A[mid] < target && target <= A[right])
                    left = mid+1;
                else
                    right = mid-1;
            }else if (A[left] == A[mid])//1 3 1 1 1
                ++left;
            else//A[mid] == A[right]
                --right;
        }
        return false;
    }
```

 

