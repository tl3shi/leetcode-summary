# Combination Sum II

题目来源：[combination Sum II](https://oj.leetcode.com/problems/combination-sum-ii/)

>
	Given a collection of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
	Each number in C may only be used once in the combination.	
	Note:
	All numbers (including target) will be positive integers.
	Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
	The solution set must not contain duplicate combinations.
	For example, given candidate set 10,1,2,7,6,1,5 and target 8, 
	A solution set is: 
	[1, 7] 
	[1, 2, 5] 
	[2, 6] 
	[1, 1, 6] 

解题思路：

跟 [combination-sum](./combination-sum.html) 一样, DFS，在它的基础上，将用过的跳过即可。重复的数字，后面的要跳过，不然结果有重复的。

```cpp
	
	void dfs(vector<vector<int> > &result, vector<int> &path, const vector<int> &num, int sum, int target, int start)
    {
        if(sum > target) return;
        if(sum == target)
        {
            result.push_back(path);
            return;
        }
        for(int i = start ; i < num.size(); i++)
        {
            if(sum < target)
            {
                sum += num[i];
                path.push_back(num[i]);
                dfs(result, path, num, sum, target, i+1);
                path.pop_back();
                sum -= num[i];
            }
            while(i+1 < num.size() && num[i] == num[i+1]) i++; ////ignore the next same one,so that remove the duplicated result
        }
    }
    
    vector<vector<int> > combinationSum2(vector<int> &num, int target) 
    {
         vector<vector<int> > result;
        if(num.size() == 0) return result;
        std::sort(num.begin(), num.end());
        vector<int> path;
        dfs(result, path, num, 0, target, 0);
        return move(result);
    }
```

