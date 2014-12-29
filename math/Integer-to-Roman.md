# Integer to Roman

题目来源：[Integer to Roman](https://oj.leetcode.com/problems/integer-to-roman/)

>
	Given an integer, convert it to a roman numeral.
	Input is guaranteed to be within the range from 1 to 3999.

解题思路：

跟[roman-to-integer](./roman-to-integer.html)一样，搞一个map对应关系，这个题目把一些特殊的比如4/9之类的也放进map里，然后遍历得到, 不然会搞得很复杂。 参考了[Discuss]().

```cpp
string intToRoman(int num)
{
   string vs[] = {"I", "IV", "V", "IX", "X", "XL", "L", "XC", "C", "CD", "D", "CM", "M"};
   int ks[] = {1, 4, 5, 9, 10, 40, 50, 90, 100, 400, 500, 900, 1000};
   int len = sizeof(ks)/sizeof(int);
  
   int index = len-1;
   int value = num;
   string result = "";
   while(index >= 0 && value != 0)
   {
       if(value >= ks[index])
           result += vs[index], value -= ks[index];
       else
           index--;
   }
   return result;
}
```

