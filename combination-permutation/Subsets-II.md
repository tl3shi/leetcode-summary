# Subsets II

题目来源：[Subsets II ](https://oj.leetcode.com/problems/subsets-ii/)

>
	Given a collection of integers that might contain duplicates, S, return all possible subsets.
	Note:
	Elements in a subset must be in non-descending order.
	The solution set must not contain duplicate subsets.
	For example,
	If S = [1,2,2], a solution is:
	[
	  [2],
	  [1],
	  [1,2,2],
	  [2,2],
	  [1,2],
	  []
	]

解题思路：

可以跟上题[Subsets](./subsets.html)一样做，只是在add到result的时候先判断result中是否存在。 或者最后将result unique一下都可以。

```cpp
	
	void searchWithDup(vector<vector<int> >& result, vector<int> &sub, vector<int> &S, int k, int start)
	{
	    if(sub.size() == k)
	    {
	        //also can add, at last, remove the duplicated
	        if(std::find(result.begin(), result.end(), sub) != result.end())
	            return;
	        result.push_back(sub);
	        return;
	    }
	    for(int i = start; i < S.size(); i++)
	    {
	        sub.push_back(S[i]);
	        searchWithDup(result, sub, S, k, i+1);
	        sub.pop_back();
	    }
	}
	vector<vector<int> > subsetsWithDup(vector<int> &S)
	{
	    std::sort(S.begin(), S.end());
	    vector<vector<int> > result;
	    for(int i = 0; i <= S.size(); i++)
	    {
	        vector<int> sub;
	        searchWithDup(result, sub, S, i, 0);
	    }
	    //remove the duplicated, if didnot check when add in searchWithDup
	    //std::sort(result.begin(), result.end());
	    //result.erase(std::unique(result.begin(), result.end()), result.end());
	    return move(result);
	}
```

另外，考虑到会对输入的S排序，可以在递归搜索的时候，若有连续相邻的元素，则只需要搜索一个即可。[ref](http://www.cnblogs.com/x1957/p/3517989.html)

```cpp
	
	void search(vector<vector<int> > &result, const vector<int> &S, vector<int> &input, int start, int k)
    {
        if(input.size() == k){
            result.push_back(input);
            return;
        }
        for(int i = start; i < S.size(); i++){
            if(i != start && S[i] == S[i-1]) continue;
            input.push_back(S[i]);
            search(result, S, input, i+1, k);
            input.pop_back();
        }
    }
    vector<vector<int> > subsetsWithDup(vector<int> &S) 
    {
        std::sort(S.begin(), S.end());
        vector<vector<int> > result;
        vector<int> input;
        for(int k = 0; k <= S.size(); k++)
            search(result, S, input, 0, k);
        return move(result);
    }
```

