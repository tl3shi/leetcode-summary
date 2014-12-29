# Valid Parentheses

题目来源：[Valid Parentheses](https://oj.leetcode.com/problems/valid-parentheses/)

>
	Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
	The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

解题思路：

用stack. 

```cpp
bool isValid(string s) 
{
   stack<char> ss;
   for(int i = 0; i < s.length(); i++)
   {
       switch(s[i])
       {
           case '(':
           case '[':
           case '{':
               ss.push(s[i]);
               break;
           case ')':
               if(!ss.empty() && ss.top() == '(')
                   ss.pop();
               else
                   return false;
               break;
           case ']':
               if(!ss.empty() && ss.top() == '[')
                   ss.pop();
               else
                   return false;
               break;
           case '}':
               if(!ss.empty() && ss.top() == '{')
                   ss.pop();
               else
                   return false;
               break;
           default:
               return false;
       }
   }
   return ss.empty();
}
```

 

