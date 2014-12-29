# Word Ladder II

题目来源：[Word Ladder II](https://oj.leetcode.com/problems/word-ladder-ii/)

>

    Given two words (start and end), and a dictionary, find all shortest
    transformation sequence(s) from start to end, such that:
    Only one letter can be changed at a time
    Each intermediate word must exist in the dictionary
    For example,
    Given:
    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]
    Return
    [
        ["hit","hot","dot","dog","cog"],
        ["hit","hot","lot","log","cog"]
    ]
    Note:
    All words have the same length.
    All words contain only lowercase alphabetic characters.

解题思路：

先BFS把邻接图构造出来，即比如与hit相差紧1个字符的单词有哪些~ 然后再dfs把所有结果搜索出来。有了[word ladder](http://tanglei.me/leetcode/word-ladder.html)的经验，这次就直接用`26*length(word)`去查找相邻的单词而不取dict搜索了。 其实到可以判断下 dict大小和 `26*length(word)`之间的关系决定选用哪种方法。

```cpp
	
	void getDiff1s(string s, unordered_set< string> &adjlist , const unordered_set< string> &dict )
	{
	    for(int i = 0; i < s.length(); i++)
	    {
	        string strback(s );
	        for(char c = 'a'; c <= 'z'; c++)
	        {
	            strback[i] = c;
	            auto it = dict .find(strback);
	            if(it != dict .end() && *it != s && adjlist.find(*it) == adjlist .end())
	                adjlist.insert(strback);
	        }
	    }
	}
	void genResult(int level, int targetLen , string end, vector <string> & path, std::unordered_map <string, unordered_set<std::string >> &adjList, vector<vector <string> > & result)
	{
	    string curStr = path[path .size() - 1];
	    if(level == targetLen)
	    {
	        if(curStr == end )//!!IMPORTANT
	            result.push_back(path );
	        return;
	    }
	    for(auto it = adjList[curStr].begin(); it != adjList [curStr].end(); ++it)
	    {
	        path.push_back(*it);
	        genResult( level+1, targetLen , end, path, adjList, result);
	        path.pop_back();
	    }
	}
	
	
	vector<vector <string>> findLadders( string start , string end, unordered_set <string> & dict)
	{
	    std::unordered_map< string, unordered_set <std::string>> adjList;
	    if(dict.find( end) != dict .end()) dict.insert( end);
	    if(dict.find( start) != dict .end()) dict.erase( start);
	    //build adjList
	    unordered_set< string> twoLevels[2];
	    twoLevels[0].insert( start);
	    int level = 0;
	    while ( true)
	    {
	        unordered_set<string > &lastLevel = twoLevels[level % 2];
	        unordered_set<string > &nextLevel = twoLevels[(level+1) % 2];
	        nextLevel.clear();
	        for(auto it = lastLevel.begin(); it != lastLevel.end(); ++it)
	        {
	            unordered_set<string > adj;
	            getDiff1s(*it, adj, dict);
	            adjList[*it] = adj;
	            nextLevel.insert(adj.begin(), adj.end()); //if the same, will not insert
	        }
	        if(nextLevel.size() == 0)
	            return vector <vector< string>>();// no result
	        //can remove the ones in dict of the current level,
	        for(auto it = nextLevel.begin(); it != nextLevel.end(); ++it)
	            dict.erase(*it);//erase by key
	        ++level;
	        if(nextLevel.find(end ) != nextLevel.end())//find the smallest path
	            break;
	    }
	    vector< vector<string > > result;
	    vector< string> path(1, start );
	    //adjList contains the smallest path, but not all the path is valid,
	    //valid: path's length is level AND the last one is end 
	    genResult(0, level, end, path, adjList, result);
	    return move(result);
	}
```

get了一种bfs的新技能，用一个queue，不用像上面那样两层之间交换。 一层一层之间加个特殊的节点表示层次之间的隔板（比如空指针啊，空串等）。
上面其他逻辑不变，bfs部分改变后的代码如下，也能AC。 
针对本体的逻辑，注意最内层for循环(//!!!!!)，不能直接加到q1中去，因为这样操作q1中可能含有重复的单词，会超时。

```cpp
	
	vector<vector <string>> findLadders( string start , string end, unordered_set <string> & dict)
	{
	    std::unordered_map< string, unordered_set <std::string>> adjList;
	    if(dict.find( end) != dict .end()) dict.insert( end);
	    if(dict.find( start) != dict .end()) dict.erase( start);
	    //build adjList
	    queue< string> q1;
	    q1.push( start);
	    int level = 0;
	    while (!q1.empty())
	    {
	        q1.push(""); //"" or NULL to split cur level and next level
	        bool toEnd = false;
	        unordered_set<string> toDelete;
	        while(q1.front() != "")
	        {
	            string it = q1.front(); q1.pop();
	            unordered_set<string > adj;
	            getDiff1s(it, adj, dict);
	            adjList[it] = adj;
	            for(auto it = adj.begin(); it != adj.end(); it++)
	            {
	                //q1.push(*it); //!!!!! this way may TLE
	                toDelete.insert(*it);
	                if(*it == end) toEnd = true;
	            }
	        }
	        if(toDelete.size() == 0) return vector<vector <string>>();
	        for(auto it = toDelete.begin(); it != toDelete.end(); it++)
	        {
	            q1.push(*it);
	            dict.erase(*it);
	        }
	        q1.pop(); // pop ""
	        ++level;
	        if(toEnd)//find the smallest path
	            break;
	    }
	    vector< vector<string > > result;
	    vector< string> path(1, start );
	    //adjList contains the smallest path, but not all the path is valid,
	    //valid: path's length is level AND the last one is end 
	    genResult(0, level, end, path, adjList, result);
	    return move(result);
	}
```

