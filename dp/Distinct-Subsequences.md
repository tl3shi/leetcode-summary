# Distinct Subsequences

题目来源：[Distinct Subsequences](https://oj.leetcode.com/problems/distinct-subsequences/)

>

    Given a string S and a string T, count the number of distinct subsequences of T
    in S.
    A subsequence of a string is a new string which is formed from the original
    string by deleting some (can be none) of the characters without disturbing the
    relative positions of the remaining characters. (ie, "ACE" is a subsequence of
    "ABCDE" while "AEC" is not).

    Here is an example:
    S = "rabbbit", T = "rabbit"
    Return 3.

解题思路：

动态规划, `dp[j][i]` 表示`S[:i],T[:j]`的结果, dp[j][i]至少为dp[j][i-1]
那么 若`S[i] == T[j]`, 则dp[j][i]还得加上dp[j-1][i-1]即S[:i-1],T[:j-1]的匹配结果。

```cpp
	
	int numDistinct(string S, string T)
    {
        int n = S.length();
        int m = T.length();
        if(m >= n) return T == S ? 1 : 0;
        vector<vector<int> > dp(m, vector<int>(n, 0));
        //dp[j][i] S[:i] T[:j] matches
        for(int i = 0; i < n; i++)
            for(int j = 0; j < m; j++)
            {
                if(i >= 1)
                    dp[j][i] = dp[j][i-1];
                if(S[i] == T[j])
                {
                    if(j >= 1 && i >= 1)
                        dp[j][i] += dp[j-1][i-1];
                    if(j == 0)
                        dp[j][i] += 1;
                }
            }
        return dp[m-1][n-1];
    }
```

若以dp[j][i]中的i/j以长度来看的话，代码要简洁些。
初始化dp[0][0:i]=1 表示T中长度为0的串可以和S中任意长度匹配。

```cpp
	
	int numDistinct(string S, string T)
    {
        int m = T.length();
        int n = S.length();
        if(m >= n) return T == S;
        vector<vector<int> > dp(m+1, vector<int>(n+1, 0));
        for(int i = 0; i <=n; i++)
            dp[0][i] = 1;
        for(int i = 1; i <= n; i++)
            for(int j = 1; j <= m; j++)
                dp[j][i] = dp[j][i-1] + (S[i-1] == T[j-1] ? dp[j-1][i-1] : 0);
        return dp[m][n];
    }
```

节省内存

```cpp

	int numDistinct(string S, string T) 
    {
        int m = T.length();
        int n = S.length();
        if (m > n) return 0;    // impossible for subsequence
        
        vector<int> path(m+1, 0);
        path[0] = 1;            // initial condition
        for (int j = 1; j <= n; j++) {
            // traversing backwards so we are using path[i-1] from last time step
            for (int i = m; i >= 1; i--) {
                path[i] = path[i] + (T[i-1] == S[j-1] ? path[i-1] : 0);
            }
        }
        return path[m]; 
    }
```

这题参考了[REF](https://oj.leetcode.com/discuss/2143/any-better-solution-that-takes-less-than-space-while-in-time?show=2143#q2143)，其实跟[Interleaving String](./interleaving-string.html) 这道题差不多。

