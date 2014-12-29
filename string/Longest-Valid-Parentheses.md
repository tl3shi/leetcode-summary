# Longest Valid Parentheses

题目来源：[Longest Valid Parentheses](https://oj.leetcode.com/problems/longest-valid-parentheses/)

>
	Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
	For "(()", the longest valid parentheses substring is "()", which has length = 2.
	Another example is ")()())", where the longest valid parentheses substring is "()()", which has length = 4.

解题思路：

找连续合法的括号对数。

###  O(2\*N)

1、用一个数组记录每个括号的配对状态，借助stack找配对的index，最后再扫描一遍，找连续配对的数量max.[ref1](https://oj.leetcode.com/discuss/5907/an-easy-understanding-way-to-solve-it).

```cpp
	
	int longestValidParentheses(string s) 
    {
        stack<int> left;
        vector<bool> match(s.length(), false);
        for(int i = 0; i < s.length(); i++)
        {
            if(s[i] == '(')
                left.push(i);
            else//')'
            {
                if(! left.empty())
                {
                    match[left.top()] = true; left.pop();
                    match[i] = true;
                }//else default false
            }
        }
        int result = 0;
        for(int i = 0; i < s.length(); i++)
        {
            int len = 0;
            while(i < s.length() && match[i]) i++, len++;
            result = std::max(result, len);
        }
        return result;
    }
```

###  O(N)


用last记录上一个还没配对的右括号”)”, 用一个栈记录下”(“的index, 遇到”)”, 配对时pop掉，记录其长度, pop完时，长度为当前 `index-last`, 没完时，长度为当前`index-stack.top()`. [ref2](http://www.cnblogs.com/lichen782/p/leetcode_Longest_Valid_Parentheses.html)

例如:

	`)(()())` last＝0, index=3时, pop(),len=3-left.top()=2, 
	index=5时, pop(),len=5-left.top()=4, 
	index=6时, empty() len=6-last=6.

```cpp
	
	int longestValidParentheses(string s) 
    {
        stack<int> left;
        int result = 0;
        int last = -1;
        for(int i = 0; i < s.length(); i++)
        {
            if(s[i] == '(')
                left.push(i);
            else//')'
            {
                if(left.empty())
                    last = i;
                else
                {
                    left.pop();
                    int len = 0;
                    if(left.empty())
                        len = i - last;
                    else
                        len = i - left.top();
                    result = std::max(result, len);
                }
            }
        }
        return result;
    }
```

