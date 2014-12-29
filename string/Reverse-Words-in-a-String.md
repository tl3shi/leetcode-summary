# Reverse Words in a String


>Given an input string, reverse the string word by word.
For example,
Given s = "the sky is blue",
return "blue is sky the".

解题思路：类似矩阵转置的操作 (AB)^t = B^tA^t

例如 “hello world”.reverse = “dlrow olleh” 
然后针对每一个word进行reverse，拼接而成得到”world hello”

注意的地方: 
1. 全是空格的情况； 
2. 中间单词间隔多个空格； 
3. reverse最后一个单词。

```cpp
void reverseWords(string &s)
{
    int start = 0;
    while(s[start] == ' ') start++;
    int end = (int)s.length() - 1;
    while(s[end] == ' ') end--;
    if(end < start)//1.
    {
        s = "";
        return;
    } //if all blank
    s = s.substr(start, end-start+1); //trim
    std::reverse(s.begin(), s.end());
    s += ' '; //3. for the last word
    string result;
    start = 0;
    int i = 0;
    while(i < s.length())
    {
        if(s[i] == ' '){
            string tmp = s.substr(start, i-start+1);//tmp including '_'(blank)
            std::reverse(tmp.begin(), tmp.end());//'_word1_word2'
            result += tmp;
            while(i < s.length() && s[i] == ' ') i++; //2.
            if(i == s.length()) 
                break;
            start = i;
        }else
            i++;
    }
    s = result.substr(1, result.length()-1);
}
```
从[discuss](https://oj.leetcode.com/discuss/3378/is-my-solution-good-enough)里面还看到了简短的代码～值得学习。 通过stringstream 一次提取一个单词出来, 然后将这个单词与上一次的结果连接(逆序)。

```cpp
void reverseWords2(string &s)
{
    stringstream ss(s);
    string tmp = "";
    string result = "";
    while(ss >> tmp)
    {
        tmp += " ";
        tmp += result;
        result = tmp;
    }
    s = result.substr(0, result.length()-1);
}
```


