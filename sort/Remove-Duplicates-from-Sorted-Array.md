# Remove Duplicates from Sorted Array

题目来源：[Remove Duplicates from Sorted Array](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-array/)

>
	Given a sorted array, remove the duplicates in place such that each element appear only once and return the new length.
	Do not allocate extra space for another array, you must do this in place with constant memory.
	For example,
	Given input array A = [1,1,2],
	Your function should return length = 2, and A is now [1,2].

解题思路：

```cpp
	
	int removeDuplicates(int A[], int n) 
    {
        if(n <= 1) return n;
        int index = 0;
        int i = 0;
        while(i < n)
        {
            while(i+1 < n && A[i+1] == A[i])
                i++;
            //A[i+1] != A[i] // 1 1 2
            A[index++] = A[i++];
        }
        return index; //index
    }
```



