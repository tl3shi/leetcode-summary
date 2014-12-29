# Restore IP Addresses

题目来源：[Restore IP Addresses](https://oj.leetcode.com/problems/restore-ip-addresses/)

>
    Given a string containing only digits, restore it by returning all possible
    valid IP address combinations.
    For example:
    Given "25525511135",
    return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)

解题思路：
在原串中加点，每个位置都去试探，直到3个点加完毕，若满足规则就是。
注意以0开头的段。

```cpp

	bool check(const string &str)
	{
	    if(str.length() == 0) return false;
	    int num = std::stoi(str);
	    if(str[0] == '0' && str.length() != 1)
	        return false;
	    if(num >= 0 && num <= 255)
	        return true;
	    return false;
	}
	
	void search(vector<string> &result, string prefix, const string &input, int start, int dot)
	{
	    if(input.length() - start > (4-dot) * 3) return;
	    if(dot == 3)
	    {
	        string str = input.substr(start, input.length()-start);
	        if(check(str))
	            result.push_back(prefix + str);
	        return;
	    }
	    
	    for(int i = start; i < (start+3) && i < input.length(); i++)
	    {
	        string str = input.substr(start, i-start+1);
	        if(check(str))
	            search(result, prefix + str + ".", input, i+1, dot+1);
	        
	    }
	}
	
	vector<string> restoreIpAddresses(string s)
	{
	    vector<string> result;
	    if(s.length() < 4 || s.length() > 12) return result;
	    string prefix = "";
	    search(result, prefix, s, 0, 0);
	    return move(result);
	}
```



