# String to Integer (atoi)

题目来源：[String to Integer (atoi)](https://oj.leetcode.com/problems/string-to-integer-atoi/)

>
	Implement atoi to convert a string to an integer.
	Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.
	Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
	Requirements for atoi:
	The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.
	The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.
	If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.
	If no valid conversion could be performed, a zero value is returned. If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned.

解题思路：

注意的问题：

- 前面的空格, 正负数；
- 字符串前面的字符部分匹配了数字，返回这部分匹配的，忽略后面非法的。
- 越界问题。INT_MAX (2147483647) or INT_MIN (-2147483648) is returned. 

###  从后往前

```cpp
int atoi(const char *str) 
{
   int len = strlen(str);
   int startIndex = 0;
   while(startIndex < len && str[startIndex] == ' ')
       ++startIndex;
   if(startIndex == len) return 0;
   int sign = 1;
   if(str[startIndex] == '-' || str[startIndex] == '+')
       sign = (str[startIndex] == '-' ? -1 : 1), ++startIndex;
   if (!(str[startIndex] >= '0' && str[startIndex] <= '9')) return 0;
   int endIndex = startIndex;
   for(endIndex = startIndex; endIndex < len; endIndex++)
       if (!(str[endIndex] >= '0' && str[endIndex] <= '9')) break;
   --endIndex;
   long long result = 0L; long long base = 1L;
   for(int i = endIndex; i >= startIndex; i--, base *= 10)
   {
       result += (str[i]-'0')*base;
       if(result > INT_MAX) return sign == 1 ? INT_MAX : INT_MIN;//break;
   }
   result *= sign;
   //if (result >= INT_MAX) return INT_MAX;
   //if (result <= INT_MIN) return INT_MIN;
   return result;
}
```

上面的解法从后往前，注意base可能越界。也可以用下面的解法，从前往后。

###  从前往后

```cpp
int atoi(const char *str)
{
    if(*str == '\0') return 0;
    while(* str == ' ' ) str++; //trim blank
    bool nagative = false;
    if(*str == '-')
    {
        nagative = true;
        str++;
    }
    else if(*str == '+') //ignore '+'
        str++;
    long long result = 0L;
    while(* str != '\0' )
    {
        if(!(*str >= '0' && * str <= '9' ))
            break;
        result *= 10;
        result += (* str - '0' );
        if(result > INT_MAX ) return nagative ? INT_MIN : INT_MAX ;
        str++;
    }
    if(nagative) result = -result;
    return ( int)result;
}
```

若不用long long的话，可以在```*10 + ```之前先判断是否越界即 ```result > INT_MAX/10 || result == INT_MAX/10 && *str-'0'> INT_MAX%10 ```
