# Regular Expression Matching

题目来源：[Regular Expression Matching](https://oj.leetcode.com/problems/regular-expression-matching/)

>
	Implement regular expression matching with support for '.' and '*'.
	'.' Matches any single character.
	'*' Matches zero or more of the preceding element.
	The matching should cover the entire input string (not partial).
	The function prototype should be:
	bool isMatch(const char *s, const char *p)
	Some examples:
	isMatch("aa","a") → false
	isMatch("aa","aa") → true
	isMatch("aaa","aa") → false
	isMatch("aa", "a*") → true
	isMatch("aa", ".*") → true
	isMatch("ab", ".*") → true
	isMatch("aab", "c*a*b") → true

解题思路：

注意理解请题意，\* 和前面的字符是一个整体, c\* 可以表示'', 'c','ccccc' 等。'.*' 表示 '[......]'

```cpp
	
	bool isMatch(const char *s, const char *p) 
    {
        if(s == NULL && p == NULL) return true;
        if(s == NULL || p == NULL) return false;
        if(*p == '\0') return *s == '\0';
        if(*(p+1) == '*')
        {
            //.* ----> .[......]
            while(*s == *p || (*s != '\0' && *p == '.'))
            {
                if(isMatch(s, p+2))
                    return true;
                ++s;
            }
            return isMatch(s, p+2);
        }else if(*s == *p || (*s != '\0' && *p == '.'))
            return isMatch(s+1, p+1);
        return false;
    }
```

