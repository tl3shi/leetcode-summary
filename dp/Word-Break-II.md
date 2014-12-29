# Word Break II

题目来源：[Word Break II](https://oj.leetcode.com/problems/word-break-ii/)

>

    Given a string s and a dictionary of words dict, add spaces in s to construct a sentence where each word is a valid dictionary word.

	Return all such possible sentences.
	
	For example, given
	s = "catsanddog",
	dict = ["cat", "cats", "and", "sand", "dog"].
	
	A solution is ["cats and dog", "cat sand dog"].

解题思路：

沿用[Word break](word-break.html)的思路，dp[i]表示s中0到i的串能在dict中对应，首先想到的是用vector把dp[i]为true的情况都保存下来(即以i为结尾的单词)，最后组装回去可得到结果。注意不能每次得到dp[i]为true就去枚举结果，这样会超时(最后可能没有成功走到结尾也浪费了时间在这里去拼装)。

代码如下：

```cpp

	 void searchResult(string input, vector<vector<string> >&dp, int len, vector<string> &result)
    {
        if(len <= 0) 
        {
            if(len == 0)
                result.push_back(input);
            return;
        }
        for(int i = 0; i < dp[len].size(); i++)
        {
            string str = dp[len][i];
            if(input.length() > 0)
                searchResult(str + " " + input, dp, len - str.length(), result);
            else
                searchResult(str, dp, len - str.length(), result);
        }
    }
    vector<string> dp(string s, unordered_set<string> &dict)
    {
        int n = s.length();
        vector<bool> dp(n+1, false);
        dp[0] = true;
        vector<vector<string> > dpStrings(n+1, vector<string>());
        for(int j = 1; j <= n; j++)
            for(int i = 0; i < j; i++)
            {
                if(dp[i]) //dp[i], true, dp[i] && s[i:j]==> dp[j]
                {
                    string str = s.substr(i, j-i);
                    if(dict.find(str) != dict.end())
                    {
                        dp[j] = true;
                        //break;, can NOT break, for wordbreak II should return all the possible solutions
                        dpStrings[j].push_back(str);
                    }
                }
            }
        vector<string> result;
        if(dp[n])
            searchResult("", dpStrings, n, result);
        return result;
    }
    vector<string> wordBreak(string s, unordered_set<string> &dict) {
        return dp(s, dict);
    }
```

其实，按照上面提的思路一边dp的时候就去枚举结果也是可以的，测试用例中就那一个较长的过不了，先按照wordbreak的思路detective一下再枚举就可以AC。(一般人我不告诉他) :)

```cpp
	
	//中途的复杂度记录dps的复杂度较高，用例（aaaaaaaaaaaaaaaa*b, aaaaaa...aaa）可能最后没有结果 但仍然搜索了很多次，导致超时或内存超过
	//先detect一下 可以通过oj
	vector<string> wordBreak2(string s, unordered_set<string> &dict)
	{
	    if(! wordBreak(s, dict))
	        return vector<string>();
	    size_t len = s.length();
	    vector<bool> dp(len+1, false);
	    dp[0] = true; //dp[i] : s[0:i] is ok
	    vector< vector<string> > dps(len+1);
	    for(int i = 1; i <= len; i++)
	    {
	        for(int j = 0; j < i; j++)
	        {
	            if(dp[j]) // dp[0:j] ok + s[j:i] ok ---> dp[i] is ok
	            {
	                string sub =  s.substr(j, i-j);
	                if(dict.find(sub) != dict.end())
	                {
	                    dp[i] = true;
	                    if(dps[j].size() > 0)
	                    {
	                        for(auto it = dps[j].begin(); it != dps[j].end(); it++)
	                            dps[i].push_back(string((*it) + " "+ sub));
	                    }else
	                    {
	                        dps[i].push_back(sub);
	                    }
	 
	                }
	            }
	        }
	    }
	    return dps[len];
	}
```

