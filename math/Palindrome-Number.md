# Palindrome Number

题目来源：[Palindrome Number](https://oj.leetcode.com/problems/palindrome-number/)

>
	Determine whether an integer is a palindrome. Do this without extra space.
	Some hints:
	Could negative integers be palindromes? (ie, -1)
	If you are thinking of converting the integer to string, note the restriction of using extra space.
	You could also try reversing an integer. However, if you have solved the problem "Reverse Integer", you know that the reversed integer might overflow. How would you handle such case?
	There is a more generic way of solving this problem.

解题思路：

常量空间~ 关键得到长度,然后求reverse的数字，判断是否相等。

```cpp
bool isPalindrome(int x) 
{
   if (x < 0) return false;
   if (x < 10) return true;
   int len = 0;
   long long base = 10L;
   int xbak = x;
   while(x/base)
       base *= 10;
   base /= 10;
   x = xbak;
   long long reverse = 0;
   int base2 = 1;
   while(base)
   {
       reverse += (x / base % 10) * base2;
       base2 *= 10;
       base /= 10;
   }
   return reverse == x;
}
```
 
