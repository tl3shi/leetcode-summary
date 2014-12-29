# Palindrome Partitioning II

题目来源：[Palindrome Partitioning II](https://oj.leetcode.com/problems/palindrome-partitioning-ii/)

>

    Given a string s, partition s such that every substring of the partition is a
    palindrome.
    Return the minimum cuts needed for a palindrome partitioning of s.
    For example, given s = "aab",
    Return 1 since the palindrome partitioning ["aa","b"] could be produced using 1 cut.

解题思路：

>

	Calculate and maintain 2 DP states:
	pal[i][j] , which is whether s[i..j] forms a pal
    d[i], which is the minCut for s[i..n-1]
	Once we comes to a pal[i][j]==true:
        if j==n-1, the string s[i..n-1] is a Pal, minCut is 0, d[i]=0;
        else: the current cut num (first cut s[i..j] and then cut the rest s[j+1...n-1]) is 1+d[j+1], 
             compare it to the exisiting minCut num d[i], repalce if smaller.
    d[0] is the answer.

第一步还是跟[Palindrome Partitioning](./palindrome-partitioning.html)一样，用DP，任意i-j组合先计算好是否是回文；

第二步仍用DP，dp[i]表示s[i, len-1]最少的minCut, 对每一个palindrome[i][j]为true的:

* if j == len-1, 则 dp[i]=0;
* else s要拆分为s[i, j], [j+1, len-1],当前cut数=1+dp[j+1], 所以dp[i] = std::min(dp[i], 1+dp[j+1])

当然这两步也可以合在一起. [ref](https://oj.leetcode.com/discuss/6691/my-dp-solution-explanation-and-code)

```cpp

	int minCut(string s) 
    {
        int n = s.length();
        vector<vector<bool> > dp(n, vector<bool>(n, false));
        for(int i = 0; i < n; i++)
            dp[i][i] = true;
        vector<int> cuts(n, 0);
        for(int i = n-1; i >= 0; i--)
        {   
            cuts[i] = n-i-1;
            for(int j = i; j < n; j++)
            {
                if(s[i] == s[j] && ((i+1>j-1) || dp[i+1][j-1] ))
                {
                    dp[i][j] = true;
                    if(j == n-1)
                        cuts[i] = 0;
                    else //cut s[:j][j+1:n]
                        cuts[i] = std::min(cuts[i], 1 + cuts[j+1]);
                }
            }
        }
        return cuts[0];
    }
```

