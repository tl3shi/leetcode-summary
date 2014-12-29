# Remove Element

题目来源：[Remove Element](https://oj.leetcode.com/problems/remove-element/)

>
	Given an array and a value, remove all instances of that value in place and return the new length.
	The order of elements can be changed. It doesn't matter what you leave beyond the new length.

解题思路：

直接两个index, 跟目标不同就复制下, 不然只移动后面一个index.
跟[Remove Duplicates from Sorted Array](./remove-duplicates-from-sorted-array.html)这道题类似.

```cpp
int removeElement(int A[], int n, int elem) 
{
    int index = 0;
    for(int i = 0; i < n; i++)
        if(A[i] != elem)
            A[index++] = A[i];
    return index;
}
```

