# Interleaving String

题目来源：[Interleaving String](https://oj.leetcode.com/problems/interleaving-string/)

>
    Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.
    For example,
    Given:
    s1 = "aabcc",
    s2 = "dbbca",
    When s3 = "aadbbcbcac", return true.
    When s3 = "aadbbbaccc", return false.

解题思路：

### 递归

超时。

```cpp
bool isInterleave(string s1, string s2, string s3)
{
    return isInterleave(s1, s1.length()-1, s2, s2.length()-1, s3, s3.length()-1);
}
bool isInterleave(string s1, int i1, string s2, int i2, string s, int i)
{
    if(i < 0 || i1 < 0 || i2 < 0) return i < 0 && i1 < 0 && i2 < 0;
    if((s1[i1] == s[i]) && isInterleave(s1, i1-1, s2, i2, s, i-1))
        return true;
    if((s2[i2] == s[i]) && isInterleave(s1, i1, s2, i2-1, s, i-1))
        return true;
    return false;
}
```

###  动态规划

DP。

用DP，类似[Distinct Subsequences](./distinct-subsequences.html) 一样，
dp[i][j]表示长度为i的s1[0:i-1],长度为j的s2[0:j-1]和s3[0:i+j-1]的匹配结果，那么 
	
	dp[i][j] = dp[i][j-1] && (s2[j-1]==s3[i+j-1]) 
           || dp[i-1][j] && (s1[i-1]==s3[i+j-1]) 
           or false.
注意边界的初始化条件.

```cpp
bool isInterleave(string s1, string s2, string s3) 
{
    int n1 = s1.length(); int n2 = s2.length(); int n3 = s3.length();
    if(n1 + n2 != n3) return false;
    if(n1 == 0) return s2 == s3;
    if(n2 == 0) return s1 == s3;
    vector<vector<bool> > dp(n1+1, vector<bool>(n2+1, false));
    dp[0][0] = true;
    for(int i = 1; i <= n1; i++)
        dp[i][0] = (s1[i-1] == s3[i-1]);
    for(int i = 1; i <= n2; i++)
        dp[0][i] = (s2[i-1] == s3[i-1]);
    for(int i = 1; i <= n1; i++)
        for(int j = 1; j <= n2; j++)
        {
            if(s1[i-1] == s3[i+j-1] && dp[i-1][j])
                dp[i][j] = true;
            else if(s2[j-1] == s3[i+j-1] && dp[i][j-1])
                dp[i][j] = true;
            else 
                dp[i][j] = false;
        }
    return dp[n1][n2];
}
```


