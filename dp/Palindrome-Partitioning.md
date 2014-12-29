# Palindrome Partitioning

题目来源：[Palindrome Partitioning](https://oj.leetcode.com/problems/palindrome-partitioning/)

>

    Given a string s, partition s such that every substring of the partition is a
    palindrome.

    Return all possible palindrome partitioning of s.

    For example, given s = "aab",
    Return

    [
        ["aa","b"],
        ["a","a","b"]
    ]

解题思路：

###  直接暴力解决

枚举每种可能，去判读是否回文。跟[排列组合](http://tanglei.me/tags.html#排列组合-ref)算法一样。
还可以优化，把中间的某个子串是否回文用hash缓存下来。

```cpp

    bool isPalindrome(string s)
    {
        int n = s.length();
        if(n <= 1) return true;
        int left = 0; int right = n-1;
        while(left < right)
        {
            if(s[left] == s[right])
            {
                left++;
                right--;
            }else
                return false;
        }
        return true;
    } 
    void search(vector<string> &path, int start, string s, vector<vector<string> > &result)
    {
        int n = s.length();
        if(start > n) return;
        if(start == n) 
        {
            result.push_back(path);
            return;
        }
        for(int i = start; i < n; i++)
        {
            string str = s.substr(start, i-start+1);
            if(isPalindrome(str))
            {
                path.push_back(str);
                search(path, i+1, s, result);
                path.pop_back();
            }
        }
    }
    vector<vector<string>> partition(string s)
    {
        vector<vector<string> > result;
        vector<string> path;
        search(path, 0, s, result);
        return move(result);
    }

```

###  利用动态规划 O(n^2)

`dp[i:j]`表示`s[i:j]`是回文,  如果`s[i] == s[j] and dp[i+1, j-1]`,满足条件, 则dp[i:j]就是回文。 
注意要先算dp[i+1][j-1]，所以循环的顺序。

```cpp

	void search(vector<string> &path, int start, string s, vector<vector<bool> > &dp, vector<vector<string> > &result)
	{
	    if(start == s.length()){
	        result.push_back(path);
	        return;
	    }
	    for(int i = start; i < s.length(); i++)
	    {
	        if(dp[start][i]){
	            string sub = s.substr(start, i-start+1);
	            path.push_back(sub);
	            search(path, i+1, s, dp, result);
	            path.pop_back();
	        }
	    }
	}
	vector<vector<string>> partitionDp(string s)
	{
	    int n = s.length();
	    vector<vector<bool> > dp(n, vector<bool>(n, false));
	    for(int i = 0; i < n; i++) //init, single char is palindrome
	        dp[i][i] = true;
	    //dp[i:j] s[i:j] is palindrome,  need dp[i+1, j-1], i need i+1, should downto, j need j-1, should upto
	    for(int i = n-1; i >= 0; i--)
	        for(int j = i; j < n; j++)
	        {
	            if(s[i] == s[j] && ( (i+1 >j-1) || dp[i+1][j-1]))
	                dp[i][j] = true;
	        }
	    vector<vector<string> > result;
	    vector<string> path;
	    search(path, 0, s, dp, result);
	    return move(result);
	}
```

其实像上面那样把每一个回文子串找出来后，就不用像排列组合那样去搜索了，可以直接构造。这个参考了[leetcode-cpp](https://github.com/soulmachine/leetcode)。
`result[i]` 表示s[i:n]构成的回文串拆分结果。再走一遍dp就可以构造出来。方法如下:
result[i]的结果为当前的回文串 插入每一个 result[i+1]构成。
 
```cpp
	
	vector<vector<string>> partitionDp(string s)
    {
        int n = s.length();
        vector<vector<bool> > dp(n, vector<bool>(n, false));
        for(int i = 0; i < n; i++) //init, single char is palindrome
            dp[i][i] = true;
        //dp[i:j] s[i:j] is palindrome,  need dp[i+1, j-1], i need i+1, should downto, j need j-1, should upto
        for(int i = n-1; i >= 0; i--)
            for(int j = i; j < n; j++)
            {
                if(s[i] == s[j] && ( (i+1 >j-1) || dp[i+1][j-1]))
                    dp[i][j] = true;
            }
        vector<vector<vector<string> >> result(n, vector<vector<string> >());
        for(int i = n-1; i >= 0; i--)
            for(int j = i; j < n; j++)
            {
                if(dp[i][j])
                {
                    string str = s.substr(i, j-i+1);
                    if(j+1 < n)
                    {
                        vector<vector<string> > &next = result[j+1];
                        for(int k = 0; k < next.size(); k++)
                        {
                            auto v = next[k];
                            v.insert(v.begin(), str);
                            result[i].push_back(v);
                        }
                    }
                    else
                        result[i].push_back(vector<string>(1, str));
                }
            }
        return result[0];
    }

```

