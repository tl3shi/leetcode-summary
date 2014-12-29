# Permutation Sequence

题目来源：[Permutation Sequence](https://oj.leetcode.com/problems/permutation-sequence/)

>
	The set [1,2,3,…,n] contains a total of n! unique permutations.
	By listing and labeling all of the permutations in order,
	We get the following sequence (ie, for n = 3):
	"123"
	"132"
	"213"
	"231"
	"312"
	"321"
	Given n and k, return the kth permutation sequence.
	Note: Given n will be between 1 and 9 inclusive.

解题思路：

	康托展开的逆运算
	既然康托展开是一个双射，那么一定可以通过康托展开值求出原排列，即可以求出n的全排列中第x大排列。
	如n=5,x=96时：
	首先用96-1得到95，说明x之前有95个排列.(将此数本身减去！)
	用95去除4! 得到3余23，说明有3个数比第1位小，所以第一位是4.
	用23去除3! 得到3余5，说明有3个数比第2位小，所以是4，但是4已出现过，因此是5.
	用5去除2!得到2余1，类似地，这一位是3.
	用1去除1!得到1余0，这一位是2.
	最后一位只能是1.
	所以这个数是45321.

代码如下：

```cpp
	
	void jiecheng(vector<int> &f, int n)
    {
        f.resize(n+1);
        f[0]=1;
        for(int i = 1; i <= n; i++)
            f[i] = f[i-1]*i;
    }
    string getPermutation(int n, int k) 
    {
        vector<int> f;
        jiecheng(f, n);
        string result;
        vector<int> small(n, 0);
        for(int i = 1; i <= n; i++)
            small[i-1] = i;
        k -= 1;
        for(int i = 0; i < n; i++)
        {
            int bigger = k / f[n-i-1];
            k = k % f[n-i-1];
            result += (*(small.begin()+bigger) + '0');
            small.erase((small.begin()+bigger));
        }
        return result;
    }
```


参考 
- [康托展开](http://baike.baidu.com/view/437641.htm)
- [Leetcode: Permutation Sequence](http://blog.csdn.net/doc_sgl/article/details/12840715)
http://blog.csdn.net/MrRoyLee/article/details/34981399 


