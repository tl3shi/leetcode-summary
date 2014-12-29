# Longest Substring Without Repeating Characters

题目来源：[Longest Substring Without Repeating Characters](https://oj.leetcode.com/problems/longest-substring-without-repeating-characters/)

>
	Given a string, find the length of the longest substring without repeating characters. For example, the longest substring without repeating letters for "abcabcbb" is "abc", which the length is 3. For "bbbbb" the longest substring is "b", with the length of 1.

解题思路：

记录上一次出现同字符到当前字符的长度，如下图。
![](http://tl3shi.github.com/resource/blogimage/leetcode-longest-substring-without-repeating-characters.png)

```cpp
int lengthOfLongestSubstring(string s) 
{
   if(s.length() <= 1) return s.length();
   vector<int> table(256, -1); 
   int start = 0;
   int result = 0;
   for(int i = 0; i < s.length(); i++)
   {
       if(table[s[i]] >= start)
           start = table[s[i]]+1;
       result = std::max(result, i-start+1);
       table[s[i]]=i;
   }
   return result;
}
```

注意数组初始化, ```int table[256]={-1}; //只有第一个为-1，其他为0.```

我不会告诉你我参考了[这篇文章的](http://blog.csdn.net/likecool21/article/details/10858799).

