# Longest Common Prefix

题目来源：[Longest Common Prefix](https://oj.leetcode.com/problems/longest-common-prefix/)

>
	Write a function to find the longest common prefix string amongst an array of strings.

解题思路：

从前往后一个一个对比就是。

```cpp
string longestCommonPrefix(vector<string> &strs)
{
   if (strs.size() == 0) return "";
   if (strs.size() == 1) return strs[0];
   if (strs[0].length() == 0) return "";
   int size = 0;
   while(size < strs[0].length())
   {
       char ch = strs[0][size];
       for(int i = 1; i < strs.size(); i++)
           if(size >= strs[i].length() || strs[i][size] != ch)
               return strs[0].substr(0, size);
       size++;
   }
   return strs[0].substr(0, size);
}
```

 
