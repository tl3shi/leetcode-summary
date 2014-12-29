# Implement strStr()

题目来源：[Implement strStr()](https://oj.leetcode.com/problems/implement-strstr/)

>
	Implement strStr().
	Returns a pointer to the first occurrence of needle in haystack, or null if needle is not part of haystack.

解题思路：

###  暴力法 \\( O(m*n)\\)

```cpp
char *strStr(char *haystack, char *needle) 
{
   assert(haystack != NULL && needle != NULL);
   char * result = NULL;
   int n = strlen(haystack);
   int m = strlen(needle);
   for(int i = 0; i <= n-m; i++)
   {
       int j = 0;
       for(; j < m; j++)
       {
           if(haystack[i+j] != needle[j])
               break;
       }
       if(j == m)
           {result = haystack + i; return result;}
   }
   return result;
}
```

###  KMP, \\( O(m + n) \\)

[这篇文章](http://blog.csdn.net/v_july_v/article/details/7041827) 讲得比较详细.

```cpp
void getNext(char * p, vector<int> &next)
{
   int m = next.size();
   if(m == 0) return;
   int k = -1;
   int j = 0;
   while(j < m-1)
   {
       if(k == -1 || p[j] == p[k])
       {
           ++j;++k;
           next[j] = p[j] != p[k] ? k : next[k]; 
       }else
           k = next[k];
   }
}
int kmpSearch(char * s, char * p)
{
   int m = strlen(p);
   vector<int> next(m, -1);
   getNext(p, next);
   int n = strlen(s);
   int i = 0; int j = 0;
   while(i < n && j < m)
   {
       if(j == -1 || s[i] == p[j])
           ++i, ++j;
       else
           j = next[j];
   }
   if(j == m)
       return i - j;
   return -1;
}
char *strStr(char *haystack, char *needle) 
{
   assert(haystack != NULL && needle != NULL);
   char * result = NULL;
   int index = kmpSearch(haystack, needle);
   if(index == -1)
       return result;
   return haystack + index;
}
```

这里的参考资料还不错： 

- [邓俊辉老师讲的这个](https://www.xuetangx.com/c4x/TsinghuaX/30240184_2X/asset/11.String.C1.Kmp.memorization.pdf) 还不错～可以参考下. 
- [还有这个视频也不错](http://v.youku.com/v_show/id_XNzQzMjQ1OTYw.html) ～
- [july的这篇文章](http://blog.csdn.net/v_july_v/article/details/7041827)

<!-- MathJax Section -->
<script type="text/javascript"
src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>
