# Edit Distance

题目来源：[Edit Distance](https://oj.leetcode.com/problems/edit-distance/)

>
	Given two words word1 and word2, find the minimum number of steps required to convert word1 to word2. (each operation is counted as 1 step.)
	You have the following 3 operations permitted on a word:
	a) Insert a character
	b) Delete a character
	c) Replace a character
	
解题思路：

编辑距离是动态规划里面的经典题目。
DP, DP[i][j] 表示word1[0:i-1] 与 word2[0:j-1]的编辑距离。[Ref](http://en.wikipedia.org/wiki/Edit_distance)
![](http://upload.wikimedia.org/math/4/1/1/411039fdd7ca16f4569c10310156cfc2.png)
w(del), w(ins), w(sub) 分别是删除，插入，替换(substitute)的权重。

```cpp
	
	int minDistance(string word1, string word2) 
    {
        int m = word1.length();
        int n = word2.length();
        vector<vector<int> >dp(m+1, vector<int>(n+1, 0));
        //dp[i][j]: word1[0:i-1] -> word2[0:j-1]
        for(int i = 0; i <= m; i++)
            dp[i][0] = i;//insert
        for(int i = 0; i <= n; i++)
            dp[0][i] = i;
        for(int i = 1; i <= m; i++)
            for(int j = 1; j <= n; j++)
            {
                if(word1[i-1] == word2[j-1])
                    dp[i][j] = dp[i-1][j-1];
                else{
                    int insert = dp[i-1][j] + 1; //insert word2[j] to word1[i]
                    int _delete = dp[i][j-1] + 1; //delete word1[i]
                    int replace = dp[i-1][j-1] + 1; //replace word1[i] to word2[j]
                    dp[i][j] = std::min(replace, std::min(insert, _delete));
                }
            }
        return dp[m][n];
        
    }
```

关于更多编辑距离的算法及应用可参考 [stanford 课件](http://www.stanford.edu/class/cs124/lec/med.pdf)。

