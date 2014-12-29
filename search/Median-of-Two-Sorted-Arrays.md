# Median of Two Sorted Arrays

题目来源：[Median of Two Sorted Arrays](https://oj.leetcode.com/problems/median-of-two-sorted-arrays/)

>
	There are two sorted arrays A and B of size m and n respectively. Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

解题思路：

`log` 得二分了。
思想是将A[k/2-1] 与 B[k/2-1]比较：如果 `A[k/2-1] < B[k/2-1]` 意味着, A[0: k/2-1] 不会大于合并后的第k个数。

```cpp
	
	//kth number, increase. k starts from 1
    int findkth(int *a, int m, int *b, int n, int k)
    {
        if(m > n) return findkth(b, n, a, m, k);
        //m < n
        if(m == 0) return b[k-1];
        if(k == 1) return std::min(a[0], b[0]);
        int ka = std::min(m, k>>1);
        int kb = k - ka;
        if(a[ka-1] < b[kb-1])
            return findkth(a+ka, m-ka, b, n, k-ka);
        else if (a[ka-1] > b[kb-1])
            return findkth(a, m, b+kb, n-kb, k-kb);
        return a[ka-1];
    }
    
    double findMedianSortedArrays(int a[], int m, int b[], int n) 
    {
        assert(!(m == 0 && n == 0));
        if ((m+n)&0x1)
            return findkth(a, m, b, n, ((m+n)>>1)+1);
        return  (findkth(a, m, b, n, ((m+n)>>1)+1) + findkth(a, m, b, n, (m+n)>>1))*0.5;
    }
```


