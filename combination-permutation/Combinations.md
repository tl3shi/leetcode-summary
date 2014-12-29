# Combinations

题目来源：[Combinations](https://oj.leetcode.com/problems/combinations/)

>
	Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
	For example,
	If n = 4 and k = 2, a solution is:
	
	[
	  [2,4],
	  [3,4],
	  [2,3],
	  [1,2],
	  [1,3],
	  [1,4],
	]

解题思路：

```cpp
	
	void search(vector<vector<int> > &result, vector<int> &input, int start, int k, int n)
    {
        if(input.size() == k){
            result.push_back(input);
            return;
        }
        for(int i = start; i <= n; i++){
            input.push_back(i);
            search(result, input, i+1, k, n);
            input.pop_back();
        }
    }
    vector<vector<int> > combine(int n, int k) 
    {
        vector<vector<int> > result;
        assert(k <= n);
        vector<int> input;
        search(result, input, 1, k, n);
        return move(result);
    }
```
 

