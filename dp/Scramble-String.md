# Scramble String

题目来源：[Scramble String ](https://oj.leetcode.com/problems/scramble-string/)

>
	Given a string s1, we may represent it as a binary tree by partitioning it to two non-empty substrings recursively.
	Below is one possible representation of s1 = "great":
	    great
	   /    \
	  gr    eat
	 / \    /  \
	g   r  e   at
	           / \
	          a   t
	To scramble the string, we may choose any non-leaf node and swap its two children.
	For example, if we choose the node "gr" and swap its two children, it produces a scrambled string "rgeat".
	    rgeat
	   /    \
	  rg    eat
	 / \    /  \
	r   g  e   at
	           / \
	          a   t
	We say that "rgeat" is a scrambled string of "great".
	Similarly, if we continue to swap the children of nodes "eat" and "at", it produces a scrambled string "rgtae".
	    rgtae
	   /    \
	  rg    tae
	 / \    /  \
	r   g  ta  e
	       / \
	      t   a
	We say that "rgtae" is a scrambled string of "great".
	Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.

解题思路：
	
用递归即可。 rg|tae gr|eat， rg和gr是scramble， tae和eat递归成 t|ae 和 ea|t， 因此最后满足条件。

```cpp
	
	bool isSameChar(string s1, string s2)
    {
        int x[26] = {0};
        for(int i = 0; i < s1.length(); i++)
            ++x[s1[i]-'a'];
        for(int i = 0; i < s2.length(); i++)
            --x[s2[i]-'a'];
        for(int i = 0; i < 26; i++)
        {
            if(x[i] != 0) return false;
        }
        return true;
    }
    bool isScramble(const string &s1, const string &s2)
    {
        if(s1.length() != s2.length()) return false;
        if(s1 == s2) return true;
        if(! isSameChar(s1, s2)) return false;
        int n = s1.length();
        for(int i = 1; i < n; i++)
        {
            if(isScramble(s1.substr(0, i), s2.substr(0, i)) && isScramble(s1.substr(i, n-i), s2.substr(i, n-i)))
                return true;
            if(isScramble(s1.substr(0, i), s2.substr(n-i, i)) && isScramble(s1.substr(i, n-i), s2.substr(0, n-i)))
                return true;
        }
        return false;
    }
```

虽然能AC，但上面的代码效率确实～ 内存耗费不少吧，每次都去创建string出来。
参考下别人的代码，直接用迭代器来做，省掉了字符串的创建。
以上还可以把一些算过的用map cache起来, 学下 [STL的tuple](http://en.cppreference.com/w/cpp/utility/tuple)。

```cpp
	
	bool isSameChar(string::const_iterator first1, string::const_iterator first2, int len)
    {
        int x[26] = {0};
        for(auto i = first1; i != first1+len; i++)
            ++x[*i-'a'];
        for(auto i = first2; i != first2+len; i++)
            --x[*i-'a'];
        for(int i = 0; i < 26; i++)
        {
            if(x[i] != 0) return false;
        }
        return true;
    }
    bool isScramble(string::const_iterator first1, string::const_iterator first2, int len)
    {
        if(len == 1) return *first1 == *first2;
        if(! isSameChar(first1, first2, len)) return false;
        for(int i = 1; i < len; i++)
        {
            if( (isScramble(first1, first2, i) && isScramble(first1+i, first2+i, len-i))
              ||(isScramble(first1, first2+len-i, i) && isScramble(first1+i, first2, len-i)))
              return true;
        }
        return false;
    }
    bool isScramble(const string &s1, const string &s2)
    {
        if(s1.length() != s2.length()) return false;
        if(s1 == s2) return true;
        return isScramble(s1.begin(), s2.begin(), s1.length());
    }
```

设状态为 f[n][i][j]，表示长度为 n，起
点为 s1[i] 和起点为 s2[j] 两个字符串是否互为 scramble，则状态转移方程为

	f[n][i][j] = (f[k][i][j] && f[n-k][i+k][j+k])
			|| (f[k][i][j+n-k] && f[n-k][i+k][j])
跟上面递归的`isScramble(string::const_iterator first1, string::const_iterator first2, int len)`一致。

```cpp
	
	bool isScramble(const string &s1, const string &s2)
	{
	    if(s1.length() != s2.length()) return false;
	    if(s1 == s2) return true;
	    int n = s1.length();
	    //dp[n][i][j], s1[i:i+n), s2[j:j+n) is scramble
	    vector<vector<vector<bool> > > dp(n+1, vector<vector<bool>>(n, vector<bool>(n, false)));
	    for(int i = 0; i < n; i++)
	        for(int j = 0; j < n; j++)
	            dp[1][i][j] = s1[i] == s2[j];
	    for(int len = 2; len <= n; len++)
	        for(int i = 0; i <= n-len; i++)
	            for(int j = 0; j <= n-len; j++)
	                for(int k = 1; k < len; k++)
	                {
	                    if( (dp[k][i][j] && dp[len-k][i+k][j+k]) ||
	                        (dp[k][i][j+len-k] && dp[len-k][i+k][j]))
	                        {
	                            dp[len][i][j] = true;
	                            break;
	                        }
	                }
	    return dp[n][0][0];
	}
```

参考 [leetcode-cpp](https://github.com/soulmachine/leetcode)

