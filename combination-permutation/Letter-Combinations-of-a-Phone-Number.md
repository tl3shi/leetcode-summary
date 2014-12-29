# Letter Combinations of a Phone Number

题目来源：[Letter Combinations of a Phone Number](https://oj.leetcode.com/problems/letter-combinations-of-a-phone-number/)

>
	Given a digit string, return all possible letter combinations that the number could represent.
	A mapping of digit to letters (just like on the telephone buttons) is given below.
![](http://upload.wikimedia.org/wikipedia/commons/thumb/7/73/Telephone-keypad2.svg/200px-Telephone-keypad2.svg.png)
>
	Input:Digit string "23"
	Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
	Note:
	Although the above answer is in lexicographical order, your answer could be in any order you want.

解题思路：

排列组合问题.

```cpp
void dfs(vector<string> &result, string &str, int start, const string &input, const vector<string> &numMap)
{
    if (start == input.length())
    {
        result.push_back(str);
        return;
    }
    int num = input[start] - '0';
    for(int i = 0; i < numMap[num].size(); i++)
    {
        str[start] = numMap[num][i];
        dfs(result, str, start+1, input, numMap);
    }
}

vector<string> letterCombinations(string digits)
{
    vector<string> numMap({"","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"});
    vector<string> result;
    int n = digits.length();
    if (n == 0) return vector<string>(1, "");//special case in oj
    string str(n, '.');
    dfs(result, str, 0, digits, numMap);
    return move(result);
}
```
 

