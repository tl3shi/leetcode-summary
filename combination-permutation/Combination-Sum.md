# Combination Sum

题目来源：[combination Sum](https://oj.leetcode.com/problems/combination-sum/)

>
	Given a set of candidate numbers (C) and a target number (T), find all unique combinations in C where the candidate numbers sums to T.
	The same repeated number may be chosen from C unlimited number of times.
	Note:
	All numbers (including target) will be positive integers.
	Elements in a combination (a1, a2, … , ak) must be in non-descending order. (ie, a1 ≤ a2 ≤ … ≤ ak).
	The solution set must not contain duplicate combinations.
	For example, given candidate set 2,3,6,7 and target 7, 
	A solution set is: 
	[7] 
	[2, 2, 3] 

解题思路：

深搜, 排序后一个一个往里面加，注意是组合，比如当前加到2了，2还可以加，但2以前的就不能加了。

```cpp
	
	void dfs(vector<vector<int> > &result, vector<int> &path, const vector<int> &num, int sum, int target)
    {
        if(sum > target) return;
        if(sum == target)
        {
            result.push_back(path);
            return;
        }
        for(int i = 0 ; i < num.size(); i++)
        {
            if(sum < target && (path.size() == 0 || num[i] >=path[path.size()-1]))
            {
                sum += num[i];
                path.push_back(num[i]);
                dfs(result, path, num, sum, target);
                path.pop_back();
                sum -= num[i];
            }
        }
    }
    
    vector<vector<int> > combinationSum(vector<int> &candidates, int target) 
    {
        vector<vector<int> > result;
        if(candidates.size() == 0) return result;
        std::sort(candidates.begin(), candidates.end());
        vector<int> path;
        dfs(result, path, candidates, 0, target);
        return move(result);
    }
```

