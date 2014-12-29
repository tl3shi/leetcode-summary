# Divide Two Integers

题目来源：[Divide Two Integers](https://oj.leetcode.com/problems/divide-two-integers/)

>
	Divide two integers without using multiplication, division and mod operator.

解题思路：

只能用减法了，一个一个减比较慢。
注意考虑溢出的情况～ 

>	In 2's complement systems, the absolute value of the most-negative value is out of range, e.g. for 32-bit 2's complement type int, INT_MIN is -2147483648, but the would-be result 2147483648 is greater than INT_MAX, which is 2147483647.

long的表达是4个字节～要用llabs才能AC。 [cppreference 关于abs几个函数的说明在此](http://en.cppreference.com/w/cpp/numeric/math/abs). 

```cpp
int       abs( int n );
long      abs( long n );
long long abs( long long n );
(since C++11)
long       labs( long n );
long long llabs( long long n );
```
labs参数和返回值是long, oj 4个字节不够～ 用下面的或者用llabs都可以。

```cpp
long long  m = abs((long long)divisor);
long long  n = abs((long long)dividend); 
```

```cpp
int divide(int dividend, int divisor) 
{
   int result = 0;
   int sign = ( (dividend > 0 && divisor > 0) || (dividend < 0 && divisor < 0) ) ? 1 : -1; // dividend * divisor > 0, this way be overflow
   //    long long  m = labs(divisor); this not work in leetcode's oj
 //   long long  n = labs(dividend);
   long long  m = llabs(divisor);
   long long  n = llabs(dividend); 
   if(m == 1) return sign * n;
   if(m == n) return sign;
   if(n < m) return 0;
   while(n >= m)
   {
       int pow = 1;
       int mm = m;
       while(n >= mm && mm > 0) // mm > 0 important
       {
           n -= mm;
           result += pow;
           pow <<= 1;
           mm <<= 1;
       }
   }
   return sign * result;
}
```

