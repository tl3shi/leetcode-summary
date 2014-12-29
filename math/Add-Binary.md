# Add Binary

题目来源：[Add Binary](https://oj.leetcode.com/problems/add-binary/)

>
	Given two binary strings, return their sum (also a binary string).
	For example,
	a = "11"
	b = "1"
	Return "100".

解题思路：

跟前面的 [plus-one](./plus-one.html) 差不多。 这里注意char和int的转换，别搞错了。

```cpp
	
	string addBinary(string a, string b) 
    {
        int i = 0;
        while(a[i] == ' ')  i++;
        a = a.substr(i, a.length()-i);
        i = 0;
        while(b[i] == ' ') i++;
        b = b.substr(i, b.length()-i);
        int m = a.length(); int n = b.length();
        if(m < n) return addBinary(b, a);
        if(n == 0) return a;
        string result(a);
        for(int i = n-1, j = m-1; i >= 0; i--,j--)
            result[j] = (result[j] - '0') + (b[i] - '0') + '0';
        for(int i = m-1; i >= 1; i--)
        {
            int c = result[i] - '0';
            result[i] = (c % 2) + '0';
            result[i-1] += (c / 2);
        }
        int first = result[0] - '0';
        if(first > 1)
        {
            result[0] = (first % 2) + '0';
            result = "1" + result;
        }
        return result;
    }
```


