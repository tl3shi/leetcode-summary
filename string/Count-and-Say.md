# Count and Say

题目来源：[Count and Say](https://oj.leetcode.com/problems/count-and-say/)

>
	The count-and-say sequence is the sequence of integers beginning as follows:
	1, 11, 21, 1211, 111221, ...	
	1 is read off as "one 1" or 11.
	11 is read off as "two 1s" or 21.
	21 is read off as "one 2, then one 1" or 1211.
	Given an integer n, generate the nth sequence.
	Note: The sequence of integers will be represented as a string.

解题思路：

递归数数即可。

```cpp
	
	string to_str(int a)
    {
        stringstream ss;
        ss << a;
        string result;
        ss >> result;
        return result;
    }
    
    string countAndSay(int n) 
    {
        if(n == 0) return "";
        const string str[] = {"1", "11", "21", "1211", "111221"};
        int num = sizeof(str) / sizeof(string);
        if(n-1 < num) return str[n-1];
        string last = countAndSay(n-1);
        int i = 0;
        int len = last.length();
        string result;
        while(i < len)
        {
            int count = 1;
            while(i+1 < len && last[i] == last[i+1])
                ++count, ++i;
            result += to_str(count);
            result += to_str(last[i]-'0');
            i++;
        }
        return result;
    }
```
 

