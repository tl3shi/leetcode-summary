# Pow(x, n)

题目来源：[Pow(x, n)](https://oj.leetcode.com/problems/powx-n/)

>
	Implement pow(x, n).

解题思路：

```cpp
double pow(double x, int n)  
{ 
    if(n == 0 || x == 1.0) return 1.0; 
    if(x == -1.0) return n & 0x1 == 1 ? -1 : 1; 
    if(n < 0 ) return 1.0/pow(x, -n);  
    return rpow(x, n); 
}  
double rpow(double x, int n) 
{ 
    if(n == 0) return 1.0; 
    if(n == 1) return x; 
    double r = rpow(x, n/2); 
    if(n & 0x1) 
        return r*r*x; 
    return r*r; 
} 
```

