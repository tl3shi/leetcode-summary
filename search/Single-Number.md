# Single Number

题目来源：[Single Number](https://oj.leetcode.com/problems/single-number/)

>
    
    Given an array of integers, every element appears twice except for one. Find
    that single one.

    Note:
    Your algorithm should have a linear runtime complexity. Could you implement it
    without using extra memory?

解题思路：

###  普通程序员方法

用一个hashmap数数，再遍历一次即可。

```cpp

	int singleNumber(int A[], int n) 
    {
        unordered_map<int, int> count;
        for(int i = 0; i < n; i++)
            count[A[i]]++;
        for(int i = 0; i < n; i++)
        {
            if(count[A[i]] != 2)
                return A[i];
        }
        //error
        return 0;
    }
```

###  文艺程序员方法

看题目要求不用额外的存储~ 然后所有数字出现2次～ 然后想想位运算。能想到位运算应该就差不多了。 `1^1 = 0 `

```cpp

	int singleNumber(int A[], int n) 
    {
        assert(n != 0);
        int r = A[0];
        for(int i = 1; i < n; i++)
            r ^= A[i];
        return r;
    }
```

