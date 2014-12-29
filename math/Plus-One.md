# Plus One

题目来源：[Plus One ](https://oj.leetcode.com/problems/plus-one/)

>
	Given a non-negative number represented as an array of digits, plus one to the number.
	The digits are stored such that the most significant digit is at the head of the list.

解题思路：

直接从后往前加即可。

```cpp
	
	vector<int> plusOne(vector<int> &digits)
    {
        int n = digits.size();
        if(n == 0) return digits;
        digits[n-1] += 1;
        for(int i = n-1; i >= 1; i--)
        {
            int t = digits[i];
            digits[i] = t % 10;
            if(t < 10) break;
            digits[i-1] += t / 10;
        }
        if(digits[0] < 10)
            return move(digits);
        else
        {
            digits.insert(digits.begin(), digits[0]/10);
            digits[1] = digits[1] % 10;
        }
        return move(digits);
    }
```


