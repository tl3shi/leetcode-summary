# Sqrt(x)

题目来源：[Sqrt(x)](https://oj.leetcode.com/problems/sqrtx/)

>
	Implement int sqrt(int x).
	Compute and return the square root of x.

解题思路：

### 二分

注意 可能越界Int。

```cpp
	
	int binarySearch(int x)
    {
        //(x/2)^2 >= x ==>x >=4
        int left = 0; int right = x / 2;
        while(left <= right)
        {
            long long mid = left + ((right-left)>>1);
            if(mid*mid == x) return mid;
            if(mid*mid < x)
            {
                if((mid+1)*(mid+1) > x) //(mid+1)*(mid+1) may over int
                    return mid;
                left = mid+1;
            }
            else 
                right = mid-1;
        }
        return -1; 
    }
    
    int sqrt(int x) 
    {
        assert(x >= 0);
        if(x <= 1) return x;
        return binarySearch(x);
    }
```

或者牛顿迭代法, [参考这里](http://blog.punkid.org/2008/02/28/compute-the-square-root-via-newtons-iteration/).

假设f(x)是关于X的函数:

 ![](http://tl3shi.github.com/resource/blogimage/leetcode-sqrtx.png)
 
求出f(x)的一阶导，即斜率: 

$$
f'(x)=\frac{f(x\_n)-0}{x\_n - x\_{n+1}}
$$
$$
x\_{n+1} = x\_{n} - f(x_n)
$$
>
	
	f'(x) = (f(x_n) - 0) / (x_n - x_(n+1) ==>
	x_(n+1)=x_n-(f(x_n))/(f^'(x_n)) 
	令x^2 = n，假设一关于X的函数f(x)为:
	f(X) = X^2 - n
	求f(X)的一阶导为:
	f'(X) = 2X
	代入前面求到的最终式中:
	x_(k+1) = 1/2 * (x_k + n / x_k)

其实牛顿迭代法也可以看作是泰勒公式(Taylor Series)的简化.

```cpp
	
	int sqrt(int x) 
    {
        assert(x >= 0);
        if(x <= 1) return x;
        double r = 1.0;
        while(true)
        {
            if(round(r*r) == x)
                return int(r);
            r = (r + x/r)/2.0;
        }
        return -1;
    }
```

$$
f'(x_{n}) = \frac{ \mathrm{rise} }{ \mathrm{run} } = \frac{ \mathrm{\Delta y} }{ \mathrm{\Delta x} } = \frac{ f( x_{n} ) - 0 }{ x_{n} - x_{n+1} } = \frac{0 - f(x_{n})}{(x_{n+1} - x_{n})}
$$

 
<script type="text/javascript"
src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>


