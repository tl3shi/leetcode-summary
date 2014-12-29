# 3Sum

题目来源：[3Sum](https://oj.leetcode.com/problems/3sum/)

>
	Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
	Note:
	Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
	The solution set must not contain duplicate triplets.
	    For example, given array S = {-1 0 1 2 -1 -4},
	    A solution set is:
	    (-1, 0, 1)
	    (-1, -1, 2)
    
解题思路：

可以沿用[2sum](./leetcode-two-sum.html)的思路。
排序后以当前值target为基准，从当前值后面的值中找等于-target的所有对。注意去重～

- 当前值i的去重
- search对数的时候去重

```cpp
void search(vector<std::pair<int, int> > &pairs, int start, const int target, const vector<int> &num)
{
   int end = num.size() - 1;
   while(start < end)
   {
       int sum = num[start] + num[end];
       if(sum == target)
       {
           pairs.push_back(make_pair(num[start], num[end]));
           while(start < end && num[start] == num[start+1])
               ++start;
           ++start;//[start] != [start+1]
           while(start < end && num[end] == num[end-1])
               --end;
           --end;
       }else if (sum > target)
           --end;
       else
           ++start;
   }
}

vector<vector<int> > threeSum(vector<int> &num) 
{
   int n = num.size();
   vector<vector<int> > result;
   std::sort(num.begin(), num.end());
   for(int i = 0; i < n-2; i++)
   {
       int target = - num[i];
       vector<std::pair<int, int> > pairs;
       search(pairs, i+1, target, num);
       if (!(pairs.empty()))
       {
           for(auto it = pairs.begin(); it != pairs.end(); ++it)
               result.push_back(vector<int>{num[i], it->first, it->second});
       }  
       while (i < n-2 && num[i+1] == num[i]) i++; 
   }
   return move(result);
}
```

或者直接这样：

```cpp
vector<vector<int> > threeSum(vector<int> &num) 
{
   int n = num.size();
   vector<vector<int> > result;
   std::sort(num.begin(), num.end());
   for(int i = 0; i < n-2; i++)
   {
       int begin = i+1;
       int end = n - 1;
       while(begin < end)
       {
           int sum = num[i] + num[begin] + num[end];
           if(sum > 0)
               --end;
           else if (sum < 0)
               ++begin;
           else
           {
               result.push_back(vector<int>{num[i], num[begin], num[end]});
               while(begin < end && num[begin] == num[begin+1])
                   ++begin;
               ++begin;
               while(begin < end && num[end] == num[end-1])
                   --end;
               --end;
           }
       }
       while (i < n-2 && num[i+1] == num[i]) i++;
   }
   return move(result);
}
```
 

