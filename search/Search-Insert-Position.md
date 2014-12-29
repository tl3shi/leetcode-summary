# Search Insert Position

题目来源：[Search Insert Position](https://oj.leetcode.com/problems/search-insert-position/)

>
	Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order. You may assume no duplicates in the array. Here are few examples.
	[1,3,5,6], 5 → 2
	[1,3,5,6], 2 → 1
	[1,3,5,6], 7 → 4
	[1,3,5,6], 0 → 0 

解题思路：

注意运算符优先级。mid = start + ((end - start) >> 1); 后面的括号非常有必要！>> 优先级比+低！
参考lowerBound.

```cpp
	
	int searchInsert(int A[], int n, int target)
	{
	    assert(A != NULL && n != 0);
	    int left = 0; int right = n;
	    while(left != right)
	    {
	        int mid = left + ((right - left)>>1);
	        if(A[mid] == target) return mid;
	        if(A[mid] < target)
	            left = mid+1;
	        else
	            right = mid; //NOT mid-1
	    }
	    return left;
	}
```

 

