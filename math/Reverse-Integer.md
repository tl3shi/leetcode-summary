# Reverse Integer

题目来源：[Reverse Integer](https://oj.leetcode.com/problems/reverse-integer/)

>
	Reverse digits of an integer.
	Example1: x = 123, return 321
	Example2: x = -123, return -321
	Have you thought about this?
	Here are some good questions to ask before coding. Bonus points for you if you have already thought through this!
	If the integer's last digit is 0, what should the output be? ie, cases such as 10, 100.
	Did you notice that the reversed integer might overflow? Assume the input is a 32-bit integer, then the reverse of 1000000003 overflows. How should you handle such cases?
	Throw an exception? Good, but what if throwing an exception is not an option? You would then have to re-design the function (ie, add an extra parameter).
	
解题思路：

按照 [palindrome-number](./palindrome-number.html)的思路，一样。

```cpp
int reverse(int x) 
{
  int sign = x > 0 ? 1 : -1;   
  x = abs(x);
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
  return reverse * sign;    
}
```

