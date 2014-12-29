# Single Number II

题目来源：[Single Number II](https://oj.leetcode.com/problems/single-number-ii/)

>
    
    Given an array of integers, every element appears three times except for one. Find that single one.

	Note:
	Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

解题思路：

###  普通程序员方法

用一个hashmap数数，再遍历一次即可。代码就略了。

###  文艺程序员方法

有了[Single Number](http://tanglei.me/leetcode/single-number.html)的思路，可能你会想想用位运算。不过一时半会貌似想不太出来。没关系，开一个32位数组，每个数字出现3次，相应的位肯定出现3次的整数倍。剩下的那些数对应的那个应该就是要找的了。

```cpp

	int singleNumber(int A[], int n) 
    {
        int count[32] = {0};
        for(int i = 0; i < n; i++)
            for(int j = 0; j < 32; j++)
            {
                if(A[i] & (1<<j))
                    count[j] = (count[j]+1) % 3;
            }
        int r = 0;
        for(int i = 0; i < 32; i++)
        {
            if(count[i] != 0)
                r |= (1<<i);
        }
        return r;
    }
```

###  极品程序员

从[discuss](https://oj.leetcode.com/discuss/857/constant-space-solution)看到极品程序员的答案。值得学习，不过有时候容易搞混。个人认为上面第1种(文艺)程序员的方法就不错。


```cpp

	int singleNumber(int A[], int n)
    {
        int ones = 0, twos = 0, threes = 0;
        for(int i = 0; i < n; i++)
        {
            threes = twos & A[i]; //已经出现两次并且再次出现
            twos = twos | (ones & A[i]); //曾经出现两次的或者曾经出现一次但是再次出现的
            ones = ones | A[i]; //出现一次的
           
            twos = twos & ~threes; //当某一位出现三次后，我们就从出现两次中消除该位
            ones = ones & ~threes; //当某一位出现三次后，我们就从出现一次中消除该位
        }
        return ones; //twos, threes最终都为0. ones是只出现一次的数
    }
```



另外，有题目是数组中有2个数不一样，其他都出现2次，找出这两个数。
思路是全部异或得到一个数～然后从这个数中找到一个二进制位为1的位置～（说明原来的两个数这个位不一样，一个为0，一个为1）然后根据这个位可以将原始的数组分成2组。再根据single number i的思路单独每组异或得到结果。

