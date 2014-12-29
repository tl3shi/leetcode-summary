# Merge Sorted Array

题目来源：[Merge Sorted Array](https://oj.leetcode.com/problems/merge-sorted-array/)

>
	Given two sorted integer arrays A and B, merge B into A as one sorted array.
	Note:
	You may assume that A has enough space (size that is greater or equal to m + n) to hold additional elements from B. The number of elements initialized in A and B are m and n respectively.

解题思路：
	因为A空间足够，所以直接从后往前定位就可以。只需要将B放完即可，若B放完，A也已经呆在应该待的位置了。
	
```cpp
	
	void merge(int A[], int m, int B[], int n) 
    {
        int tot = m + n - 1;
        int i = m-1;
        int j = n-1;
        while(j >= 0)
        {
            if(i>=0 && A[i] >= B[j])
                A[tot--] = A[i--];
            else
                A[tot--] = B[j--];
        }
    }
```


