# Word Break

题目来源：[Word Break](https://oj.leetcode.com/problems/word-break/)

>

    Given a string s and a dictionary of words dict, determine if s can be
    segmented into a space-separated sequence of one or more dictionary words.

    For example, given
    s = "leetcode",
    dict = ["leet", "code"].

    Return true because "leetcode" can be segmented as "leet code".

解题思路：

首先想到的就是DFS，直接挨个搜索，能走到结尾就OK。不过这样做超时了。

```cpp

	//TLE
    bool dfs(string s, int startIndex, unordered_set<string> &dict)
    {
        if(startIndex > s.length()) return false;
        if(startIndex == s.length()) return true;
        for(int i = startIndex; i < s.length(); i++)
        {
            string pre = s.substr(startIndex, i - startIndex + 1);
            if(dict.find(pre) != dict.end())
            {
                if(dfs(s, i+1, dict))
                    return true;
            }
        }
        return false;
    }
    bool wordBreak(string s, unordered_set<string> &dict) 
    {
        if(s.length() == 0) return false;
        return dfs(s, 0, dict);
    }
```

然后用DP,`dp[i]`表示s[0:i]都跟dict对应了, 对于更长的j, `dp[j]`为true的话，肯定存在i使得`dp[i]`为true 和 `s[i:j]`能在dict中找到。  
因此得到如下代码：

```cpp

	bool dp(string s, unordered_set<string> &dict)
    {
        int n = s.length();
        vector<bool> dp(n+1, false);
        dp[0] = true;
        for(int j = 1; j <= n; j++)
            for(int i = 0; i < j; i++)
            {
                if(dp[i]) //dp[i], true, dp[i] && s[i:j]==> dp[j]
                {
                    string str = s.substr(i, j-i);
                    if(dict.find(str) != dict.end())
                    {
                        dp[j] = true;
                        break;
                    }
                }
            }
        return dp[n];
    }
```


