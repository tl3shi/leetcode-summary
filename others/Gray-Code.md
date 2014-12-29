# Gray Code

题目来源：[Gray Code](https://oj.leetcode.com/problems/gray-code/)

>
	The gray code is a binary numeral system where two successive values differ in only one bit.
	Given a non-negative integer n representing the total number of bits in the code, print the sequence of gray code. A gray code sequence must begin with 0.
	For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
	00 - 0
	01 - 1
	11 - 3
	10 - 2
	Note:
	For a given n, a gray code sequence is not uniquely defined.
	For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.	
	For now, the judge is able to judge based on one instance of gray code sequence. Sorry about that.


解题思路：

###  逆序

注意观察，n每增加1，即是在n-1的结果之上，最高位加1，并按照n-1的逆序。 

	n = 1 
	0 
	1 
	n=2 
	0 0 
	0 1 
	--- 
	1 1 
	1 0 
	n=3 
	0 0 0 
	0 0 1 
	0 1 1 
	0 1 0 
	------ 
	1 1 0 
	1 1 1 
	1 0 1 
	1 0 0 

```cpp
	
	vector<int> grayCode(int n) 
    {
        assert(n>=0);
        if(n == 0) return std::move(vector<int>(1,0));
        vector<int> result;
        result.push_back(0); result.push_back(1);
        for(int i = 1; i < n; i++)
        {
            int len = result.size();
            for(int j = len-1; j >=0; j--)
                result.push_back(result[j] + (1<<i));
        }
        return move(result);
    }
```

### 公式法

[格雷码](http://zh.wikipedia.org/zh-cn/%E6%A0%BC%E9%9B%B7%E7%A0%81)

	G：格雷码  B：二进制码 
	G(N) = (B(n)/2) XOR B(n) 
	Binary Code(1011)要转换成Gray Code = (1011 >> 1) ^ 1011 = 1110 

```cpp
	
	vector<int> grayCode(int n) 
    {
        assert(n>=0);
        int len = 1 << n;//std::pow(2,n);
        vector<int> result(len, 0);
        for(int i = 1; i < len; i++)
            result[i] = (i>>1)^i;
        return move(result);
    }
```

