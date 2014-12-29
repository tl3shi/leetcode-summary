# Permutations II

题目来源：[Permutations II](https://oj.leetcode.com/problems/permutations-ii/)

>
	Given a collection of numbers that might contain duplicates, return all possible unique permutations.
	For example,
	[1,1,2] have the following unique permutations:
	[1,1,2], [1,2,1], and [2,1,1].

解题思路：

跟 [Permutations](./Permutations.html)思路差不多，分为下面几种解法。

### 置换法

跟[Permutations](./Permutations.html)一样，每一个与第一个交换～用set存结果，将重复的去掉，中途剪枝下即可AC。

```cpp
	
	void dfs(set<vector<int> > &result, vector<int> &num, int start)
	{
	    if(start >= num.size()) // >= ">"also should be put in, for the last ele.
	    {
	        result.insert(num);
	        return;
	    }
	    for(int i = start; i < num.size(); i++)
	    {
	        if(i != start && num[i] == num[i-1]) continue; //culling
	        std::swap(num[i], num[start]);
	        dfs(result, num, start+1);
	        std::swap(num[i], num[start]);
	    }
	}
	
	vector<vector<int> > permuteUnique(vector<int> &num)
	{
	    set<vector<int> > result;
	    std::sort(num.begin(), num.end());
	    dfs(result, num, 0);
	    return vector<vector<int>>(result.begin(), result.end());
	}
```

###  增量构造

或者跟permutation的方法，增量构造, 这里需要用一个map存下数量。

```cpp
	
	void dfs(vector<vector<int> > &result, const int n, vector<int> &path, unordered_map<int, int> &countMap)
    {
        if(path.size() == n)
        {
            result.push_back(path);
            return;
        }
         //for(int i = 0; i < num.size(); i++)//num has redundant numbers,cannot use thisone
        for(auto it = countMap.begin(); it != countMap.end(); it++)
        {
            int cnt = 0;
            for(auto itj = path.begin(); itj != path.end(); itj++)
            {
                if(*itj == it->first) ++cnt;
            }
            if(cnt < it->second)
            {
                path.push_back(it->first);
                dfs(result, n, path, countMap);
                path.pop_back();
            }
        }
    }
    
    vector<vector<int> > permuteUnique(vector<int> &num)
    {
        vector<vector<int> > result;
        unordered_map<int, int> countMap;
        for(auto it = num.begin(); it != num.end(); it++)
            ++countMap[*it];
        vector<int> path;
        dfs(result, num.size(), path, countMap);
        return move(result);
    }
```

###  next_permunation

自然序的下一个：1 3 5 4 2，从后往前找，找到第一个降序(从后往前看)的数字3，然后找后面的比3大的最小的数字4，交换，1 4 5 3 2，然后交换index后面的序列逆序 532->235，构成下一个自然序：1 4 2 3 5。 

```cpp
 
	bool nextPermutation(vector<int> &current)
	{
	    int end = current.size() - 1;
	    while(end-1>=0 && current[end-1] >= current[end])
	        end--;
	    if(end == 0) //5 4 3 2 1
	        return false;
	    //[end-1] < [end] 2 3 5 4 1
	    int start = end-1;//3
	    end = current.size() - 1;
	    while(current[end] <= current[start])
	        end--;
	    //[end] > [start] 4 > 3
	    std::swap(current[start], current[end]); // 2 4 5 3 1
	    std::reverse(current.begin()+start+1, current.end()); //2 4 1 3 5
	    return true;
	}
	
	vector<vector<int> > permuteUnique3(vector<int> &num)
	{
	    vector<vector<int> > result;
	    std::sort(num.begin(), num.end());
	    result.push_back(num);
	    while(nextPermutation(num))
	        result.push_back(num);
	    return std::move(result);
	}
```

