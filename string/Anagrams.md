# Anagrams

题目来源：[Anagrams](https://oj.leetcode.com/problems/anagrams/)

>
	Given an array of strings, return all groups of strings that are anagrams.
	Note: All inputs will be in lower-case.

解题思路：

变位词sort后是一样的，因此可用map存起来。

```cpp

	////[from discuss] single one is not counted yet!
	vector<string> anagrams(vector<string> &strs)
    {
        unordered_map<string, vector<string>> sortedKeyValue;
        for(int i = 0; i < strs.size(); i++)
        {
            string tmp = strs[i];
            std::sort(tmp.begin(), tmp.end());
            sortedKeyValue[tmp].push_back(strs[i]);
        }
        vector<string> result;
        auto it = sortedKeyValue.begin();
        for(; it != sortedKeyValue.end(); it++)
        {
            if((*it).second.size() <= 1) continue;
            std::copy((*it).second.begin(), (*it).second.end(), back_inserter(result));
        }
        return move(result);
    }
```
 

