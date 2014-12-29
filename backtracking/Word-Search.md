# Word Search

题目来源：[Word Search](https://oj.leetcode.com/problems/word-search/)

>
	Given a 2D board and a word, find if the word exists in the grid.
	The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.
	For example,
	Given board =
	[
	  ["ABCE"],
	  ["SFCS"],
	  ["ADEE"]
	]
	word = "ABCCED", -> returns true,
	word = "SEE", -> returns true,
	word = "ABCB", -> returns false.

解题思路：

DFS， 不能重复用，所以得标记一下某个字符是否用过。

```cpp
	
bool search(vector <string> & board, int row, int col, string word, int index, vector<vector <bool>> & used)
{
    if(index == word.length())
        return true ;
    if((row-1) >= 0 && col >=0)//up
    {
        if(!used [row-1][ col] && board [row-1][ col] == word [index])
        {
            used[row -1][col] = true;
            if(search(board , row-1, col, word , index+1, used))
                return true ;
            used[row -1][col] = false;
        }
    }
    if(row >= 0 && ( col-1)>=0) //left
    {
        if(!used [row][col-1] && board[row ][col-1] == word[index ])
        {
            used[row ][col-1] = true;
            if(search(board , row, col-1, word, index +1, used))
                return true ;
            used[row ][col-1] = false;
        }
    }
    if(row+1 < board.size() && col >= 0) //below
    {
        if(!used [row+1][ col] && board [row+1][ col] == word [index])
        {
            used[row +1][col] = true;
            if(search(board , row+1, col, word , index+1, used))
                return true ;
            used[row +1][col] = false;
        }
    }
    if(row >= 0 && col+1 < board [0].size())//right
    {
        if(!used [row][col+1] && board[row ][col+1] == word[index ])
        {
            used[row ][col+1] = true;
            if(search(board , row, col+1, word, index +1, used))
                return true ;
            used[row ][col+1] = false;
        }
    }
    return false;
}
 
bool exist(vector <string> & board, string word)
{
    int row = board.size();
    if(row == 0) return false ;
    int col = board[0].size();
    if(row * col < word.length()) return false;
    vector< vector<bool > > used(row, vector< bool>(col, false ));
	
	
    int index = 0;
    for(int i = 0; i < row; i++)
    {
        for(int j = 0; j < col; j++)
        {
            if(board [i][j] == word[index])
            {
                used[i][j] = true;
                if(search(board , i, j, word, index+1, used))
                    return true ;
                used[i][j] = false;
            }
        }
    }
    return false;
}
```

上面代码难看了点，其实可以像下面这样，简单些。 另外，可以借助[Surrounded Regions](./surrounded-regions.html)的思想，在原有矩阵的情况下加标记，最后还原即可。可以省去O(m*n)的空间。

```cpp
	
bool dfs(vector<vector<char> > &board, int i, int j,  const string &word, int index)
{
   if(index == word.length()) return true;
   if(i < 0 || j < 0 || i >= board.size() || j >= board[0].size()) return false;
   if(board[i][j] == word[index])
   {
       board[i][j] = '.';//used
       bool r = false;
       r = dfs(board, i-1, j, word, index+1);//up
       if(!r && dfs(board, i+1, j, word, index+1))//below
           r = true;
       if(!r && dfs(board, i, j-1, word, index+1))//left
           r = true;
       if(!r && dfs(board, i, j+1, word, index+1)) //right
           r = true;
       board[i][j] = word[index];//reset
       if(r) return true;
   }
   return false;
}
bool exist(vector<vector<char> > &board, string word) 
{
   assert(board.size() > 0 && board[0].size() > 0);
   for(int i = 0; i < board.size(); i++)
       for(int j = 0; j < board[0].size(); j++)
           {
               if(dfs(board, i, j, word, 0))
               return true;
           }   
   return false;
}
```

