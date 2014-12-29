# Simplify Path

题目来源：[Simplify Path](https://oj.leetcode.com/problems/simplify-path/)

>
	Given an absolute path for a file (Unix-style), simplify it.
	For example,
	path = "/home/", => "/home"
	path = "/a/./b/../../c/", => "/c"
	Corner Cases:
	Did you consider the case where path = "/../"?
	In this case, you should return "/".
	Another corner case is the path might contain multiple slashes '/' together, such as "/home//foo/".
	In this case, you should ignore redundant slashes and return "/home/foo".

解题思路：

把"//"替换成"/"然后split一下，用stack记录，".."之类的就去掉。
这个Java写起来方便些。

主要就是一些testcase能否想到。

```java	
	public  String simplifyPath(String path)
    {
        if(path == null || path.length() <= 1) return path;
        //assuming always start with "/", //skip the first "/"
        if(path.charAt(path.length()-1) == '/' )
            path = path.substring(1, path.length()-1);
        path = path.replaceAll( "//", "/" );
        String[] strs = path.split( "/");
        Stack<String> ss = new Stack<String>();
        for (int i = 0; i < strs.length; i++)
        {
            if (strs[i].equals("." ))
                continue;
            if (strs[i].equals(".." ))
            {
                if (ss.size() > 0)
                    ss.pop();
            } else
            {
                if(strs[i].length()>0)
                    ss.push(strs[i]);
            }
        }
        Stack<String> ss2 = new Stack<String>();
        while(ss.size()>0)
        {
            ss2.push(ss.pop());
        }
        String result = "";
        if(ss2.size() == 0) return "/";
        while(ss2.size() > 0)
            result += "/" + ss2.pop();
        return result;
    }
```

C++ 一样的。

```cpp
	
	string simplifyPath(string path)
	{
	    vector<string> splits;
	    int start = 0;
	    int i = 0;
	    path += "/"; //make sure the last segment can put into splits.
	    while(i < path.length())
	    {
	        if(path[i] == '/')
	        {
	            if(i - start > 0){
	                splits.push_back(path.substr(start, i-start)); //no including the current '/'(i-start+1)
	                start = i;
	            }
	            while(i+1 < path.length() && path[i+1] == '/') // ignore remain '/' of "///"
	            {
	                i += 1;
	                start = i;
	            }
	        }
	        ++i;
	    }
	    vector<string> result;
	    for(int i = 0; i < splits.size(); i++)
	        if(splits[i] == "/..")
	        {
	            if (result.size()>0)
	                result.pop_back();
	        }
	        else if(splits[i] == "/.")
	            ;
	        else
	            result.push_back(splits[i]);
	    string str_result = "";
	    for(int i = 0; i < result.size(); i++)
	        str_result += result[i];
	    if(str_result.length() == 0)
	        return "/";
	    return str_result;
	}

```

