# Valid Number

题目来源：[Valid Number](https://oj.leetcode.com/problems/valid-number/)

>
	Validate if a given string is numeric.
	Some examples:
	"0" => true
	" 0.1 " => true
	"abc" => false
	"1 a" => false
	"2e10" => true
	Note: It is intended for the problem statement to be ambiguous. You should gather all requirements up front before implementing one.

解题思路：

###  粗暴方法

自己写的代码丑陋无比，一种情况一种情况试, 实在是无参考价值。
主要是各种情况，例如：

| input | result|
|------|------|
|.123| true |
|12. |True|
|47e+6|True |
|\_\_1.\__ |True|
|. |False |
|46.e3|OJ里的 .2e81  true  0.e false  46.e3 true |
|+3 |True| 
|-.3|True |
|6e6.5 |false |

```cpp
	
	bool isNumber(const char *s)
	{
	    if(s == NULL) return false;
	    if(*s == '\0') return false;
	    while(*s == ' ')
	        s++; //skip 空格
	    if(*s == '\0') return false;
	    if(*s == '-' || *s == '+') s++;
	    bool firstnumber = false;
	    if((*s >= '0' && *s <= '9') || *s == '.')
	        firstnumber = true;
	    if(! firstnumber) return false;
	    bool has_e_before = false;
	    bool has_dot_before = *s == '.';
	    if(has_dot_before)
	    {
	        s++;
	        if (!(*s >= '0' && *s <= '9')) return false; // "."
	    }
	    while(*s != '\0')
	    {
	        if(*s >= '0' && *s <= '9')
	        {
	            s++;
	        }else if(*s == 'e')
	        {
	            if(has_e_before) return false;//.2e81  true  //0.e false  //46.e3 true
	            has_e_before = true;
	            s++;
	            if(*s == '+' || *s == '-') s++; //005047e+6 ok
	            if (!(*s >= '0' && *s <= '9')) return false; //"e." "e 1"
	        }else if(*s == ' ')
	        {
	            while(*s != '\0' && *s == ' ')
	                s++;
	            if(*s == '\0')//"  1.2  "
	                return true;
	            return false; //" 2.3  3" 
	        }else if(*s == '.') 
	        { 
	            if(has_dot_before || has_e_before) return false; 
	            has_dot_before = true; 
	            s++; 
	        }else 
	        { 
	            return false; 
	        } 
	    } 
	    return true; 
	}	
```

整理下上面的代码，可以更好看些。

```cpp

	bool isNumber(const char *s) 
    {
        if(s == NULL ) return false;
        bool isNum = false; bool isDot = false; bool isExp = false;
        const char* end = s;
        while(*end != '\0') end++;
        --end;
        while(*end == ' ') --end;
        while(*s == ' ') s++;
        
        if(*s == '+')s++;
        else if(*s == '-')s++;
        while(s <= end)
        {
            if(*s>= '0' && *s <= '9'){
                isNum = true;
            }else if(*s == '.'){
                if (isDot || isExp) return false;
                isDot = true;
            }else if(*s == 'e'){
                if(isExp||!isNum) return false;
                isExp = true;
                isNum = false;//e 后面必须得有数字
            }else if(*s == '+'||*s == '-'){
                if(*(s-1) != 'e') return false;
            }else 
                return false;
            s++;
        }
        return isNum;
    }
```   

###  利用strtod.

利用函数**strtod**. 
	
	double      strtod( const char          *str, char          **str_end );
能够一步一步提取str中能够组成的double, str_end为提取后剩下的串。这里找了一份实现, 有兴趣的可以参考下 [strtod的源码](https://code.google.com/p/retrobsd/source/browse/trunk/src/libc/stdlib/strtod.c?r=509&spec=svn509).

```cpp
	
	bool isNumber(const char *s) 
    {
        char * end;
        strtod(s, &end);
        if(end == s) return false; // "  "
        while(*end != '\0')
        {
            if(*end != ' ')
                return false;
            end++;
        }
        return true;
    }
```

###  利用自动机

可参考 [自动机实现valid-number](http://blog.csdn.net/kenden23/article/details/18696083).

	注释一下本题分多少状态吧：
	0初始无输入或者只有space的状态
	1输入了数字之后的状态
	2前面无数字，只输入了Dot的状态
	3输入了符号状态
	4前面有数字和有dot的状态
	5'e' or 'E'输入后的状态
	6输入e之后输入Sign的状态
	7输入e后输入数字的状态
	8前面有有效数输入之后，输入space的状态
	共9种状态了，难设计的是6,7,8状态。
	分好之后就好办了，设计出根据输入进行状态转换就OK了。

```cpp

	class Solution {
	public:
	     bool isNumber(const char *s) {
	          enum InputType {
	               INVALID,          // 0 Include: Alphas, '(', '&' ans so on
	               SPACE,          // 1
	               SIGN,          // 2 '+','-'
	               DIGIT,          // 3 numbers
	               DOT,               // 4 '.'
	               EXPONENT,          // 5 'e' 'E'
	          };
	          int transTable[][6] = {
	          //0INVA,1SPA,2SIG,3DI,4DO,5E
	               -1,  0,  3,  1,  2, -1,//0初始无输入或者只有space的状态
	               -1,  8, -1,  1,  4,  5,//1输入了数字之后的状态
	               -1, -1, -1,  4, -1, -1,//2前面无数字，只输入了Dot的状态
	               -1, -1, -1,  1,  2, -1,//3输入了符号状态
	               -1,  8, -1,  4, -1,  5,//4前面有数字和有dot的状态
	               -1, -1,  6,  7, -1, -1,//5'e' or 'E'输入后的状态
	               -1, -1, -1,  7, -1, -1,//6输入e之后输入Sign的状态
	               -1,  8, -1,  7, -1, -1,//7输入e后输入数字的状态
	               -1,  8, -1, -1, -1, -1,//8前面有有效数输入之后，输入space的状态
	          };
	          int state = 0;
	          while (*s)
	          {
	               InputType input = INVALID;
	               if (*s == ' ') input = SPACE;
	               else if (*s == '+' || *s == '-') input = SIGN;
	               else if (isdigit(*s)) input = DIGIT;
	               else if (*s == '.') input = DOT;
	               else if (*s == 'e' || *s == 'E') input = EXPONENT;
	               state = transTable[state][input];
	               if (state == -1) return false;
	               ++s;
	          }
	          return state == 1 || state == 4 || state == 7 || state == 8;
	     }
	};
```


