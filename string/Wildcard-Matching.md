# Wildcard Matching

题目来源：[Wildcard Matching](https://oj.leetcode.com/problems/wildcard-matching/)

>
	Implement wildcard pattern matching with support for '?' and '*'.
	'?' Matches any single character.
	'*' Matches any sequence of characters (including the empty sequence).
	The matching should cover the entire input string (not partial).
	The function prototype should be:
	bool isMatch(const char *s, const char *p)
	Some examples:
	isMatch("aa","a") → false
	isMatch("aa","aa") → true
	isMatch("aaa","aa") → false
	isMatch("aa", "*") → true
	isMatch("aa", "a*") → true
	isMatch("ab", "?*") → true
	isMatch("aab", "c*a*b") → false

解题思路：

跟 [regular-expression-matching](./regular-expression-matching.html) 类似。

###  递归

主要是考虑 “\*” 匹配任意字符的问题， 下面代码超时了。

```cpp
bool isMatch(const char *s, const char *p) 
{
    if(s == NULL && p == NULL) return true;
    if(s == NULL || p == NULL) return false;
    if(*s == '\0') return *p == '\0' || (*p == '*' && *(p+1) == '\0');
    if(*p == '\0') return *s == '\0';
    if(*p == '*')
    {
        while(*(p+1) == '*') p++;//skip all continous * 
        while(*s != '\0')
        {
            if(isMatch(s, p+1)) 
                return true;
            s++;
        }
        return *(p+1) == '\0';
    }
    while(*s != '\0' && *p != '\0' && (*s == *p || *p == '?'))
    {
        s++; p++;
    }
    if(*s == '\0' && *p == '\0') return true;
    return false;
}
```

###  迭代

Key point, compare char one by one, if not matched, and '\*' matched before, then pattern backtrace to '\*', and string backtrace to the later one of compared char of last iterative time. 
参考了 [discuss.leetcode](http://discuss.leetcode.com/questions/222/wildcard-matching).

```cpp
bool isMatch(const char *s, const char *p)
{
    if(s == NULL && p == NULL) return true;
    if(s == NULL || p == NULL) return false;
    if(*s == '\0') return *p == '\0' || (*p == '*' && *(p+1) == '\0');
    if(*p == '\0') return *s == '\0';
    const char *star_p=NULL,*star_s=NULL;
    while(*s)
    {
        if(*p == '?' || *p == *s)
        {
            ++p,++s;
        }else if(*p == '*')
        {
            //skip all continuous '*'
            while(*p == '*') ++p;
            
            if(!*p) return true; //if end with '*', its match.
            
            star_p = p; //star_p is later char of '*',
            star_s = s; //store '*' pos for string
        }else if((!*p || *p != *s)  && star_p)
        {
            s = ++star_s; //skip non-match char of string, regard it matched in '*'
            p = star_p; //pattern backtrace to later char of '*'
        }else
            return false;
    }
    //check if later part of p are all '*'
    while(*p)
        if(*p++ != '*')
            return false;
    return true;
}
```

