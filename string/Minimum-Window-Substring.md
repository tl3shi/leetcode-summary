# Minimum Window Substring

题目来源：[Minimum Window Substring](https://oj.leetcode.com/problems/minimum-window-substring/)

>
	Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).
	For example,
	S = "ADOBECODEBANC"
	T = "ABC"
	Minimum window is "BANC".
	Note:
	If there is no such window in S that covers all characters in T, return the emtpy string "".
	If there are multiple such windows, you are guaranteed that there will always be only one unique minimum window in S.
	
解题思路：

始终先找到一个包含所有T中的串，记录其window长度，然后继续往后扫面，到第二个合法的window的时候，前面begin指针往后，删除window中冗余的，期间比较window的size，记录一个最小的。有了一个window之后，后面的变化始终保持window中包含一个合法的T。 
用has[]表示找到的相应字符的数量，need[]表示T中应该有的数量。
例如：

	S＝ acbbaca, T = aba
	begin,end扫描，[acbba]ca 第一个合法window后，end继续
	到[acbbaca]发现第二个合法，begin此时指向了a，而此时has[a]=3>need[a]=2，a冗余，后移begin，has[a]--; 
	ac[bbaca]: c不包含在T中，直接略过，到b, has[b]=2>need[b]=1,b冗余，继续后移，并has[b]—;
	acb[baca]: has[b]=need[b]不能减少了，记录这个短的window,并于当前比较。
	其中end/start都只+不-，复杂度为O(n).
	
代码如下：

```cpp
	
	string minWindow(string S, string T)
	{
	    if(S.length() < T.length()) return "";
	    vector<int> need(256, 0);
	    for(int i = 0; i < T.length(); i++)
	        need[T[i]]++;
	    vector<int> has(256, 0);
	    int count = 0;
	    int windowStart = 0;
	    int minLen = INT_MAX;
	    int minStart = 0;
	    for(int windowEnd = 0; windowEnd < S.length(); windowEnd++)
	    {
	        if(need[S[windowEnd]] == 0) continue;//skip
	        if(has[S[windowEnd]] < need[S[windowEnd]])
	            ++count;
	        ++has[S[windowEnd]];
	        if(count == T.length())//a window found
	        {
	            while(windowStart < windowEnd)
	            {
	                if(need[S[windowStart]] == 0)//skip
	                {
	                    ++windowStart;
	                }else if(has[S[windowStart]] > need[S[windowStart]])
	                {
	                    --has[S[windowStart]];
	                    ++windowStart;
	                }else
	                {
	                    break;
	                }
	            }
	           
	            int len = windowEnd - windowStart + 1;
	            if(len < minLen)
	            {
	                minLen = len;
	                minStart = windowStart;
	            }
	        }
	    }
	    if(minLen == INT_MAX) return "";
	    return S.substr(minStart, minLen);
	}
```

[Ref](http://www.cnblogs.com/lichen782/p/leetcode_minimum_window_substring_3.html)

