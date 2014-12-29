# Jump Game

题目来源：[Jump Game](https://oj.leetcode.com/problems/jump-game/)

>
	Given an array of non-negative integers, you are initially positioned at the first index of the array.	
	Each element in the array represents your maximum jump length at that position.
	Determine if you are able to reach the last index.
	For example:
	A = [2,3,1,1,4], return true.
	A = [3,2,1,0,4], return false.

解题思路：

###  贪心

过每个index查看能到的最远的index，若当前最远的比遍历index还小或者相等时就走不下去了。 

```cpp
	
	bool canJump(int A[], int n) 
    {
        if(n == 0) return true;
        int max_sofar = 0;
        for(int i = 0; i < n; i++)
        {
            max_sofar = std::max(max_sofar, i + A[i]);
            if(max_sofar >= n-1) return true;
            if(max_sofar <= i) return false;
        }
        return false;
    }
```

###  动归

f[i]表示走到第A[i]时, 多余的最大步数。
```f[i] = max(f[i-1], A[i-1])-1 ```

```cpp
	
	bool canJump(int A[], int n) 
    {
        if(n == 0) return true;
        vector<int> dp(n, 0);
        for(int i = 1; i < n; i++)
        {
            dp[i] = std::max(dp[i-1], A[i-1]) - 1;
            if(dp[i] < 0) return false;
        }
        return dp[n-1] >= 0;
    }
```

