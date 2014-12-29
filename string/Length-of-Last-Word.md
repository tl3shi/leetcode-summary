# Length of Last Word

题目来源：[Length of Last Word](https://oj.leetcode.com/problems/length-of-last-word/)

>
	Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.
	If the last word does not exist, return 0.
	Note: A word is defined as a character sequence consists of non-space characters only.
	For example, 
	Given s = "Hello World",
	return 5.

解题思路：

去掉首位的空格, 从最后往前走到第一个空格或开头停止。

```cpp
int lengthOfLastWord(const char *s) 
{
    char * start = const_cast<char*>(s);
    while(*start == ' ' && *start != '\0')
        start++;
    if(*start == '\0') return 0;
    char * end = start;
    while(*(end+1) != '\0')
        end++;
    while(*end == ' ') --end;
    int len = 0;
    while(end >= start && *end !=' ')
        ++len, --end;
    return len;
}
```

这个思路用STL写就简单了, [ref](https://github.com/soulmachine/leetcode)。 [std::ptr_fun<arg type, result type> 模版取函数指针](http://www.cplusplus.com/reference/functional/ptr_fun/).

```cpp

	int lengthOfLastWord(const char *s)
	{
	    if(s == NULL || *s == '\0') return 0;
	    string str(s);
	    auto start = std::find_if(str.rbegin(), str.rend(), std::ptr_fun<int, int>(std::isalpha));
	    auto last = std::find_if_not(start, str.rend(), std::ptr_fun<int, int>(std::isalpha));
	    return std::distance(start, last);
	}
```


直接从前往后，记录每一个单词的长度，后面的单词长度会取代前面的长度，注意得跳过中间的连续空格。

```cpp
	
	int lengthOfLastWord(const char *s)
    {
        if(s == NULL || *s == '\0') return 0;
        while(*s != '\0' && *s == ' ') s++;
        if(*s == '\0') return 0;
        int len = 0;
        while(*s != '\0')
        {
            if(*s != ' ')
                len++;
            else
            {
                while(*s == ' ')
                    s++;
                if(*s == '\0')
                    break;
                len = 1; //*s != ' '
            }
            s++;
        }
        return len;
    }
```

