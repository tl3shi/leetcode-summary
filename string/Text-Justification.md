# Text Justification

题目来源：[Text Justification](https://oj.leetcode.com/problems/text-justification/)

>
	Given an array of words and a length L, format the text such that each line has exactly L characters and is fully (left and right) justified.
	You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly L characters.
	Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.
	For the last line of text, it should be left justified and no extra space is inserted between words.
	For example,
	words: ["This", "is", "an", "example", "of", "text", "justification."]
	L: 16.	
	Return the formatted lines as:
	[
	   "This    is    an",
	   "example  of text",
	   "justification.  "
	]
	Note: Each word is guaranteed not to exceed L in length.
	Corner Cases:
	A line other than the last line might contain only one word. What should you do in this case?
	In this case, that line should be left-justified.

解题思路：

一步一步来即可。注意最后一行需要特殊处理。最后一行的空格尽量留在行末，而其他行是多余的空格尽量分布在行首。

```cpp
	
	vector<string> fullJustify(vector<string> &words, int L)
	{
	    if(words.size() == 0 ) return vector<string>();
	    if(words.size() == 1 && words[0].length() == L) {return vector<string>(words);}
	    vector<string> result;
	    int curIndex = 0;
	    int lastIndex = 0;
	    int curLen = 0;
	    int realwordLen = 0;
	    while(curIndex < words.size())
	    {
	        while(curIndex < words.size() && curLen + words[curIndex].length() <= L)
	        {
	            curLen += words[curIndex].length();
	            realwordLen += words[curIndex].length();
	            if(curLen != L)
	                ++curLen;//blank
	            ++curIndex;
	        }
	        //curLen + words[curIndex].length() > L, can not use curIndex
	        {
	            int blank = L - realwordLen;
	            int wordCount = curIndex - lastIndex;
	            int eachblank = wordCount == 1 ? blank : blank / (wordCount-1);
	            int moreblank = wordCount == 1 ? 0 : blank % (wordCount-1);
	            string line;
	            string eachblankstr;
	            for(int i = 0; i < eachblank; i++)
	                eachblankstr += ' ';
	            for(int j = 0, i = lastIndex; i < curIndex; i++,j++)
	            {
	                line += words[i];
	                if(wordCount == 1 || i != curIndex-1) //last one
	                {
	                    line += eachblankstr;
	                    if(j < moreblank)
	                        line += ' ';
	                }
	            }
	            result.push_back(line);
	            lastIndex = curIndex;
	            curLen = realwordLen = 0;
	        }
	    }
	    //special deal with last line
	    string lastline = result[result.size() - 1];
	    string lastlineshould(lastline.size(), ' ');
	    bool blank = true;
	    int i = 0; int j = 0;
	    while(i < L)
	    {
	        if(lastline[i] != ' ')
	        {
	            lastlineshould[j++] = lastline[i];
	            blank = true;
	        }
	        else if(blank)
	        {
	            blank = false;
	            lastlineshould[j++] = ' ';
	        }
	        ++i;
	    }
	    result[result.size()-1] = lastlineshould;
	    return move(result);
	}
```

