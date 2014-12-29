# 4Sum

题目来源：[4Sum](https://oj.leetcode.com/problems/4sum/)

>
	Given an array S of n integers, are there elements a, b, c, and d in S such that a + b + c + d = target? Find all unique quadruplets in the array which gives the sum of target.
	Note:
	Elements in a quadruplet (a,b,c,d) must be in non-descending order. (ie, a ≤ b ≤ c ≤ d)
	The solution set must not contain duplicate quadruplets.
	    For example, given array S = {1 0 -1 0 -2 2}, and target = 0.
	    A solution set is:
	    (-1,  0, 0, 1)
	    (-2, -1, 1, 2)
	    (-2,  0, 0, 2)
	    
解题思路：

跟[3-sum](./3sum.html)思路一样，只不过这个是\\( N^2 \\) 两两组合，再去找2sum, 得注意去重。

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
vector<vector<int> > fourSum(vector<int> &num, int target) 
{
   int n = num.size();
   vector<vector<int> > result;
   if(n <= 3) return result;
   std::sort(num.begin(), num.end());
   for(int i = 0; i < n-3; i++)
   {
       if(num[i] + num[i+1] + num[i+2] + num[i+3] > target) break;
       for(int j = i+1; j < n-2; j++)
       {
           int sum = num[i] + num[j];
           vector<std::pair<int, int> > pairs;
           search(pairs, j+1, target-sum, num);
           if (!(pairs.empty()))
           {
               for(auto it = pairs.begin(); it != pairs.end(); it++)   
                   result.push_back(vector<int>{num[i], num[j], it->first, it->second});
           }
           while (j+1 < n-2 && num[j+1] == num[j]) j++;
       }
       while (i < n-3 && num[i+1] == num[i]) i++;
   }
   return move(result);
}
```

<!-- MathJax Section -->
<script type="text/javascript"
src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

