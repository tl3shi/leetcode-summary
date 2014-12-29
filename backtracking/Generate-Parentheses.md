# Generate Parentheses

题目来源：[Generate Parentheses](https://oj.leetcode.com/problems/generate-parentheses/)

>
	Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
	For example, given n = 3, a solution set is:
	"((()))", "(()())", "(())()", "()(())", "()()()"

解题思路：

用递归，一个括号一个括号放，只要有左括号在，随时都可以放；放右括号时，已经放好的左括号数量要多余已放好的右括号才可以。

```cpp
void gen(vector<string> &result, string pre, int left, int right)
{
   if(left < 0 || right < 0) return;
   if(left == 0 && right == 0)
   {
       result.push_back(pre);
       return;
   }    
   if(left > 0)
       gen(result, pre+"(", left-1, right);
   if(left < right) //  (()
       gen(result, pre+")", left, right-1);
}

vector<string> generateParenthesis(int n) 
{
   vector<string> result;
   string pre;
   gen(result, pre, n, n);
   return move(result);
}
```

