# Subsets

题目来源：[Subsets](https://oj.leetcode.com/problems/subsets/)

>
	Given a set of distinct integers, S, return all possible subsets.
	Note:
	Elements in a subset must be in non-descending order.
	The solution set must not contain duplicate subsets.
	For example,
	If S = [1,2,3], a solution is:
	[
	  [3],
	  [1],
	  [2],
	  [1,2,3],
	  [1,3],
	  [2,3],
	  [1,2],
	  []
	]

解题思路：

注意输出的每个子集要有序。

### DFS搜索

跟[Combinations](./Combinations.html)一样。

```cpp
	
	void search(vector<vector<int> > &result, vector<int> &S, vector<int> &input, int start, int k)
    {
        if(input.size() == k){
            result.push_back(input);
            return;
        }
        for(int i = start; i < S.size(); i++){
            input.push_back(S[i]);
            search(result, S, input, i+1, k);
            input.pop_back();
        }
    }
    vector<vector<int> > subsets(vector<int> &S) 
    {
        std::sort(S.begin(), S.end());
        vector<vector<int> > result;
        vector<int> input;
        for(int i = 0; i <= S.size(); i++)
            search(result, S, input, 0, i);
        return move(result);
    }
```


### 0 二进制组合

每个元素都有0/1两种状态，全部排列一下即可。例如1,2,3,4一共有2^4=16种子集，第15种(2^0+2^1+2^2+2^3)为1-4都取, 第7种`(1*(2^0)+1*(2^1)+1*(2^2)+0*(2^3))`为[1,2,3]. [ref](http://blog.csdn.net/magisu/article/details/12989531).
注意得先将S排序(当然也可以先加到result中，最后再来排序), 不然结果中的子集顺序不是升序的。

```cpp
	
	vector<vector<int> > subsets(vector<int> &S) 
    {
        std::sort(S.begin(), S.end());
        int n = std::pow(2, S.size());
        vector<vector<int> > result(n, vector<int>());
        for(int j = 0; j < S.size(); j++)
        {
            for(int i = 0; i < n; i++)
            {
                if((1 << j) & i)
                    result[i].push_back(S[j]);
            }
        }
        return move(result);
    }
```




