# Multiply Strings

题目来源：[Multiply Strings](https://oj.leetcode.com/problems/multiply-strings/)

>
	Given two numbers represented as strings, return multiplication of the numbers as a string.
	Note: The numbers can be arbitrarily large and are non-negative.

解题思路：

大正整数乘法, 题目说了非负了。
跟 [plus-one](./plus-one.html)、 [add-binary](./add-binary.html)差不多。

```cpp
	
	string multiply(string num1, string num2)
    {
        if(num1.length() * num2.length() == 0) return "";
        if(num1.length() < num2.length())
            return multiply(num2, num1);
        if(num1.length() == 1)
        {
            if(num1[0] == '0') return "0";
            if(num1[0] == '1') return num2;
        }
        if(num2.length() == 1)
        {
            if(num2[0] == '0') return "0";
            if(num2[0] == '1') return num1;
        }
        //num1.length > num2.length : num1 * num2
        int total_len = num1.length() + num2.length();
        int * result = new int[total_len];
        memset(result, 0, sizeof(int) * total_len);
        
        for(int i = num2.length()-1; i >=0; i--)
        {
            int n2 = num2[i] - '0';
            int index = total_len - (num2.length() - i);
            for(int j = num1.length()-1, jindex = 0; j >= 0; j--,jindex++)
            {
                int n1 = num1[j] - '0';
                int m = n2 * n1;
                result[index - jindex] += m;
            }
        }
        int index = total_len-1;
        while(index -1 >= 0)
        {
            int m = result[index];
            result[index] = m % 10;
            result[index-1] += (m / 10);
            index--;
        }
        string str = "";
        int i = 0;
        while(result[i] == 0) //skip first 0
            i++;
        while(i < total_len)
        {
            str += (result[i] + '0');
            i++;
        }
        delete [] result;
        return str;
    }
```

 


