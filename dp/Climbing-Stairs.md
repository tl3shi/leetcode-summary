# Climbing Stairs

题目来源：[Climbing Stairs](https://oj.leetcode.com/problems/climbing-stairs/)

>
	You are climbing a stair case. It takes n steps to reach to the top.
	Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

解题思路：

设f(x)=【剩x阶时，迈楼梯的方法总数】。首先迈出第一步，如果一次迈一阶，剩下x-1阶，方法总数为f(x-1)；如果一次迈两阶，剩下x-2阶，方法总数为f(x-2); f(x)=f(x-1)+f(x-2)。容易发现，f(1)=1，f(2)=2。

```cpp
  	
	//TLE
    int climbStairsTLE(int n) 
    {
        if(n <= 1) return n;
        if(n == 2) return 2;
        return climbStairs(n-1) + climbStairs(n-2);
    }
    
```


```cpp

    int climbStairs(int n) 
    {
        if(n <= 1) return n;
        if(n == 2) return 2;
        int a = 1, b = 2, c = 2;
        for(int i = 2; i < n; i++)
        {
            c = a + b;
            a = b;
            b = c;
        }
        return c;
    }
```

