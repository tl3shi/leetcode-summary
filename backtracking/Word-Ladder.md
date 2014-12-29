# Word Ladder

题目来源：[Word Ladder](https://oj.leetcode.com/problems/word-ladder/)

>

    Given two words (start and end), and a dictionary, find the length of shortest
    transformation sequence from start to end, such that:
    Only one letter can be changed at a time
    Each intermediate word must exist in the dictionary
    For example,
    Given:
    start = "hit"
    end = "cog"
    dict = ["hot","dot","dog","lot","log"]
    As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
    return its length 5.
    Note:
    Return 0 if there is no such transformation sequence.
    All words have the same length.
    All words contain only lowercase alphabetic characters.

解题思路：

###  bfs

用BFS搜索，记录从开始到当前路径长度。注意遍历map/set删除满足条件的element的写法。第一个用BFS搜索到的肯定是最短的之一。DFS则不是哦。

```cpp

	bool diff1char(string s1, string s2)
    {
        assert(s1.length() == s2.length());
        int diff = 0;
        for(int i = 0; i < s1.length(); i++)
            if (s1[i] != s2[i]) {
                ++diff;
                if(diff == 2) return false;
            }
        return true;
    }
    int ladderLength(string start, string end, unordered_set<string> &dict)
    {
        queue<std::pair<string,int>> queues;
        queues.push(std::pair<string, int>(start,1));
        auto it = dict.find(start);
        if(it != dict.end()) dict.erase(start);
        while (queues.size() > 0)
        {
            string s = queues.front().first;
            int curLen = queues.front().second;
            queues.pop();
            if (diff1char(s, end))
                return curLen + 1;
            for(auto it = dict.begin(); it != dict.end(); )
            {
                if (diff1char(s, *it))
                {
                    queues.push(std::pair<string, int>(*it, curLen+1));
                    it = dict.erase(it);
                }else
                    ++it;
            }
        }
        return -1;
    }
```

悲剧的是，上面的过不了～ testcase中dict太大，而word相对较短，去从dict去搜索相邻的单词，耗时太久。改为变动word中的每一个字符(26个一个一个试)，然后再去dict中判断是否存在。这样就能AC。[ref](https://oj.leetcode.com/discuss/7348/time-limit-exceeded-bfs), 代码如下：

```cpp

	void getDiff1chars(string s1, queue<std::pair<string,int>> &next, int nextLen, unordered_set<string> &dict)
    {
        int n = s1.length();
        for(int i = 0; i < n; i++)
        {
            string s2(s1);
            for(char c = 'a'; c <= 'z'; c++)
            {
                if(s2[i] != c){
                    s2[i] = c;
                    auto it = dict.find(s2);
                    if(it != dict.end())
                    {
                        next.push(std::pair<string,int>(s2, nextLen));
                        dict.erase(it);
                    }
                }
            }
        }
    }
    int ladderLength(string start, string end, unordered_set<string> &dict)
    {
        queue<std::pair<string,int>> queues;
        queues.push(std::pair<string, int>(start,1));
        auto it = dict.find(start);
        if(it != dict.end()) dict.erase(start);
        while (queues.size() > 0)
        {
            string s = queues.front().first;
            int curLen = queues.front().second;
            queues.pop();
            if (diff1char(s, end))
                return curLen + 1;
            getDiff1chars(s, queues, curLen+1, dict);
        }
        return 0;
    }

```


