# Remove Duplicates from Sorted Array II

题目来源：[Remove Duplicates from Sorted Array II](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array-ii/)

>
	Follow up for "Remove Duplicates":
	What if duplicates are allowed at most twice?
	For example,
	Given sorted array A = [1,1,1,2,2,3],
	Your function should return length = 5, and A is now [1,1,2,2,3].

解题思路：

```cpp
		
	int removeDuplicates(int A[], int n)
	{
	    if(n <= 2) return n;
	    int index = 0;
	    int i = 0;
	    while(i < n)
	    {
	        int count = 1;
	        while (i+1 < n && A[i+1] == A[i])
	        {
	            count++; i++;
	        }
	        if (count >= 2)
	        {
	            A[index++] = A[i]; //A[i+1] != A[i]
	            A[index++] = A[i++];
	        } else
	            A[index++] = A[i++];
	    }
	    return index;
	}
```


```cpp

```

