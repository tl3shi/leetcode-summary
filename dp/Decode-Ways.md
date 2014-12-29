# Decode Ways

题目来源：[Decode Ways](https://oj.leetcode.com/problems/decode-ways/)

>
	A message containing letters from A-Z is being encoded to numbers using the following mapping:
	'A' -> 1
	'B' -> 2
	...
	'Z' -> 26
	Given an encoded message containing digits, determine the total number of ways to decode it.
	For example,
	Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).
	The number of ways decoding "12" is 2.
	
解题思路：

动态规划. dp[i] 表示 s[0:i-1]的结果.

1. 若当前字符s[i-1]为0
	* 若前面的字符是1或2, 则这1或2必须得跟0结合, dp[i] = dp[i-2] eg: XXX(10)
	* 若前面的字符不是1或者2, 拼接不起来了，直接return 0.
2. 当前字符不为0
	* 前面的字符为1  或者 2且当前字符为1-6. 即可分两种情况拆分, dp[i] = dp[i-2] + dp[i-1], eg: XXX16: (XXX)(16) + (XXX1)6
	* 其他, 只能自己跟自己一组了. dp[i] = dp[i-1] eg: (XXX3)6
	
还可以将下面的O(n)空间化简成常数空间～记录之前上一次结果 和 上上一次的结果，当前的结果由此获得。

```cpp
	
	int numDecodings(string s) 
    {
        if( s.empty() || s[0] == '0') return 0;
        vector<int> dp(s.length()+1, 0);
        dp[0] = 1; dp[1] = 1;
        for(int i = 2; i <= s.length(); i++)
        {
            if(s[i-1] == '0')
            {
                if(s[i-2] == '1' || s[i-2] == '2')
                    dp[i] = dp[i-2];
                else
                    return 0;
            }else if(s[i-2] == '1' || (s[i-2]=='2' && s[i-1] <= '6'))
                dp[i] = dp[i-2] + dp[i-1];
            else
                dp[i] = dp[i-1];
        }
        return dp[s.length()];
    }
```




