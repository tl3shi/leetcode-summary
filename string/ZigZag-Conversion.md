# ZigZag Conversion

题目来源：[ZigZag Conversion](https://oj.leetcode.com/problems/zigzag-conversion/)

>
	The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: (you may want to display this pattern in a fixed font for better legibility)
	P   A   H   N
	A P L S I I G
	Y   I   R
	And then read line by line: "PAHNAPLSIIGYIR"
	Write the code that will take a string and make this conversion given a number of rows:
	string convert(string text, int nRows);
	convert("PAYPALISHIRING", 3) should return "PAHNAPLSIIGYIR".

解题思路：

对勾的形式一个周期～hash一下到具体哪一个row～
	
	0			0			0
	1		5	1		5
	2	4		2	4
	3			3


```cpp
string convert(string s, int nRows)
{
   if(nRows == 1) return s;
   vector<vector<char> > rows(nRows);
   int T = nRows + nRows - 2;
   for(int i = 0; i < s.length(); i++)
   {
       int bucket = i % T;
       bucket = bucket >= nRows ? (T - bucket) : bucket;
       rows[bucket].push_back(s[i]);
   }
   string result="";
   for(int i = 0; i < nRows; i++)
   {
       for(int j = 0; j < rows[i].size(); j++)
           result += rows[i][j];
   }
   return result;
}
```

 

