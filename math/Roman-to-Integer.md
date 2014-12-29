# Roman to Integer

题目来源：[Roman to Integer](https://oj.leetcode.com/problems/roman-to-integer/)

>
	Given a roman numeral, convert it to an integer.
	Input is guaranteed to be within the range from 1 to 3999.

解题思路：

IV， I比V对应的数值小，结果就是result + （-I)，不然就是直接加 I.

学习下[unordered_map的初始化](http://zh.cppreference.com/w/cpp/language/list_initialization)

末尾加个0，让串都解析完毕。

```cpp
int romanToInt(string s) 
{
   unordered_map<char, int> kv({ {'I', 1}, {'V',5}, {'X',10}, {'L',50}, {'C',100}, {'D',500}, {'M',1000}, {'0', 0} });
   int result = 0;
   s += "0";
   for(int i = 0; i < s.length()-1; i++)
       if(kv[s[i]] < kv[s[i+1]])
           result -= kv[s[i]];
       else
           result += kv[s[i]];
   return result;
}
```
 

