# Unique Binary Search Trees

题目来源：[Unique Binary Search Trees](https://oj.leetcode.com/problems/unique-binary-search-trees/)

>
	Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
	For example,
	Given n = 3, there are a total of 5 unique BST's.
	   1         3     3      2      1
	    \       /     /      / \      \
	     3     2     1      1   3      2
	    /     /       \                 \
	   2     1         2                 3


解题思路：

###  递归

递归比较好理解。比如 根节点数字为i, 比i小的左孩纸i-1个(子问题), 右孩纸n-i. 于是就有了下面的代码。

```cpp
int numTrees(int n) 
{
    if(n == 0) return 1;//recursion, maybe, real input 0 shoule return 0
    if(n == 1) return 1;
    int r = 0;
    for(int i = 1; i <= n; i++)
        r += numTrees(i-1)*numTrees(n-i);
    return r;
}
```

###  动态规划

其实可以缓存下, 用动态规划。

```cpp
int f(int n)
{
    const int size = n+1;
    vector<int>  cache(size, 1);;
    for(int i = 2; i <=n; i++)
    {
        int result = 0;
        for(int j = 1; j <=i; j++)
            result += cache[j-1] * cache[i-j];
        cache[i] = result;
    }
    return cache[n];
}
int numTrees(int n)
{
    if(n == 0) return 0;
    return f(n);
}
```

###  数学公式法

其实这个问题有公式可以直接算的，参考[卡塔兰数](http://zh.wikipedia.org/wiki/%E5%8D%A1%E5%A1%94%E5%85%B0%E6%95%B0) 。

