# Longest Palindromic Substring

题目来源：[Longest Palindromic Substring](https://oj.leetcode.com/problems/longest-palindromic-substring/)

>
	Given a string S, find the longest palindromic substring in S. You may assume that the maximum length of S is 1000, and there exists one unique longest palindromic substring.

解题思路：

###  暴力搜索, \\(O(N^2) \\)

最简单的方法就是选中i(0~n-1)，然后向两边扩展，复杂度为\\(O(N^2) \\) . 注意回文长度可能是奇数或者偶数， 即
```aba or abba ```

```cpp
string longestPalindrome(string s) 
{
  int n = s.length();
  if (n <= 1) return s;
  int start = 0; int maxLen = 1;
  for(int i = 0; i < n; i++)
  {
      //center: i
      int left = i - 1;
      int right = i + 1;
      while(left >= 0 && right < n
          && s[left] == s[right])
          --left, ++right;
      //s[left] != s[right] , s[left+1 : right-1] is palindrome
      int len = (right-1) - (left+1) + 1;
      if(len > maxLen)
          start = left+1, maxLen = len;
      //center: between s[i] and s[i+1]
      if(i+1 < n && s[i] == s[i+1])
      {
          left = i;
          right = i+1;
          while(left >= 0 && right < n
              && s[left] == s[right])
              --left, ++right;
          len = (right-1) - (left+1) + 1;
          if(len > maxLen)
              start = left+1, maxLen = len;
      }
  }
  return s.substr(start, maxLen);
}
```

或者可以这样，将中间相同的字符跳过，不考虑奇数还是偶数的串(其实还是考虑了，也包括在内了)。
	
	abbbbbbbbba, left=1时,right一直走到最后一个b, 然后往两边判断是否相等.

```cpp
string longestPalindrome(string s) 
{
   int n = s.length();
   if (n <= 1) return s;
   int start = 0; int maxLen = 1;
   for(int i = 0; i < n; i++)
   {
       int left = i;
       int right = i;
       while(right+1 < n && s[right+1] == s[left])
           ++right;
       //s[right+1] != s[left], s[right]=s[left]
       i = right; //skip the same char
       //a[bbbbbbbb]a
       while(left-1 >= 0 && right+1 < n
           && s[left-1] == s[right+1])
           --left, ++right;
       //s[left : right] is palindrome
       int len = right - left + 1;
       if(len > maxLen)
           start = left, maxLen = len;
   }
   return s.substr(start, maxLen);
}
```

###  DP, \\(O(N^2) \\)

dp[i][j] 表示 s[i:j] 是回文, 当且尽当``` s[i] == [j] && dp[i+1][j-1]```, 即计算dp[i][j]时, dp[i+1][j-1]得先计算出来，算dp[x][i]，必须先把dp[x][i-1]先计算出来了来。


```cpp
string longestPalindrome(string s) 
{
   int n = s.length();
   if (n <= 1) return s;
   int start = 0; int maxLen = 1;
   //vector<vector<bool> > dp(n, vector<bool>(n, false));
   bool dp[1000][1000] = {false};
   for(int i = 0; i < n; i++)
       dp[i][i] = true;
   //dp[j][i]: s[j:i] is palindrome, dp[j+1][i-1] true + s[j]==s[i]
   for(int i = 1; i < n; i++)
       for(int j = 0; j < i; j++)
       {
           if(s[i] == s[j] && (j+1 > i-1 || dp[j+1][i-1]))
           {
               dp[j][i] = true;
               int len = i - j + 1;
               if(len > maxLen)
                   maxLen = len, start = j;
           }
       }
   return s.substr(start, maxLen);
}
```
计算s[:5]的结果，先得把所有s[:4]结尾的回文算出来了来。
上面比如在算dp[i][5]时，用到了dp[x][4]，在上面的循环中,dp[x][4]已经算出来了的。
另外，虽然都是平方的算法，上面用vector还过不了，用数组才能过。


###  \\( O(n) \\) 算法, Manacher 算法

[felix021的文章讲得很清楚](http://www.felix021.com/blog/read.php?2040)，这里“偷”过来。

>

	首先用一个非常巧妙的方式，将所有可能的奇数/偶数长度的回文子串都转换成了奇数长度：在每个字符的两边都插入一个特殊的符号。比如 abba 变成 #a#b#b#a#， aba变成 #a#b#a#。 为了进一步减少编码的复杂度，可以在字符串的开始加入另一个特殊字符，这样就不用特殊处理越界问题，比如$#a#b#a#（注意，下面的代码是用C语言写就，由于C语言规范还要求字符串末尾有一个'\0'所以正好OK，但其他语言可能会导致越界）。

	下面以字符串12212321为例，经过上一步，变成了 S[] = "$#1#2#2#1#2#3#2#1#";

	然后用一个数组 P[i] 来记录以字符S[i]为中心的最长回文子串向左/右扩张的长度（包括S[i]，也就是把该回文串“对折”以后的长度），比如S和P的对应关系：
	S  #  1  #  2  #  2  #  1  #  2  #  3  #  2  #  1  #
	P  1  2  1  2  5  2  1  4  1  2  1  6  1  2  1  2  1
	(p.s. 可以看出，P[i]-1正好是原字符串中回文串的总长度）
	那么怎么计算P[i]呢？该算法增加两个辅助变量（其实一个就够了，两个更清晰）id和mx，其中id表示最大回文子串中心的位置，mx则为id+P[id]，也就是最大回文子串的边界。

	然后可以得到一个非常神奇的结论，这个算法的关键点就在这里了：如果mx > i，那么P[i] >= MIN(P[2 * id - i], mx - i)。就是这个串卡了我非常久。实际上如果把它写得复杂一点，理解起来会简单很多：
	//记j = 2 * id - i，也就是说 j 是 i 关于 id 的对称点。
	if (mx - i > P[j]) 
	    P[i] = P[j];
	else /* P[j] >= mx - i */
	    P[i] = mx - i; // P[i] >= mx - i，取最小值，之后再匹配更新。
	当然光看代码还是不够清晰，还是借助图来理解比较容易。
	当 mx - i > P[j] 的时候，以S[j]为中心的回文子串包含在以S[id]为中心的回文子串中，由于 i 和 j 对称，以S[i]为中心的回文子串必然包含在以S[id]为中心的回文子串中，所以必有 P[i] = P[j]，见下图。
![](http://tl3shi.github.io/resource/blogimage/leetcode-longest-palindromic-substring-0.png)

	当 P[j] >= mx - i 的时候，以S[j]为中心的回文子串不一定完全包含于以S[id]为中心的回文子串中，但是基于对称性可知，下图中两个绿框所包围的部分是相同的，也就是说以S[i]为中心的回文子串，其向右至少会扩张到mx的位置，也就是说 P[i] >= mx - i。至于mx之后的部分是否对称，就只能老老实实去匹配了。

![](http://tl3shi.github.io/resource/blogimage/leetcode-longest-palindromic-substring-1.png)
	
	对于 mx <= i 的情况，无法对 P[i]做更多的假设，只能P[i] = 1，然后再去匹配了。
	
代码如下：

```cpp
//Manacher O(n)
//ref1: http://leetcode.com/2011/11/longest-palindromic-substring-part-ii.html
//ref2: http://blog.csdn.net/pickless/article/details/9040293
//ref3: http://www.felix021.com/blog/read.php?2040
string longestPalindrome(string s) 
{
   int len = (int)s.length() * 2 + 2;
   string news(len+1, ' ');
   news[0]='$';
   for(int i = 0; i < s.length(); i++)
   {
       news[2 * i + 1] = '#';
       news[2 * i + 2] = s[i];
   }
   news[len-1] = '#';
   news[len] = '\0';
   vector<int> p(len, 0);
   int mx = 0, id = 0;
   for(int i = 1; i < len; i++)
   {
       p[i] = mx > i ? min(p[2*id-i], mx-i) : 1;
       while(news[i + p[i]] == news[i - p[i]]) ++p[i];
       if(i + p[i] > mx)
       {
           mx = i + p[i];
           id = i;
       }
   }
   int maxLen = 0;
   int center = 0;
   for(int i = 0; i < len; i++)
   {
       if(p[i] > maxLen)
       {
           maxLen = p[i];
           center = i;
       }
   }
   return s.substr((center)/2 - maxLen/2, maxLen-1);
}
```

<!-- MathJax Section -->
<script type="text/javascript"
src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

