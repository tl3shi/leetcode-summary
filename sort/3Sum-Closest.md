# 3Sum Closest

题目来源：[3Sum Closest](https://oj.leetcode.com/problems/3sum-closest/)

>
	Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target. Return the sum of the three integers. You may assume that each input would have exactly one solution.
	    For example, given array S = {-1 2 1 -4}, and target = 1.
	    The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
	    
解题思路：

跟[3-sum](./3sum.html)思路一致。

```cpp
int threeSumClosest(vector<int> &num, int target) 
{
   int n = num.size();
   int result = 0;
   int closest = INT_MAX;
   std::sort(num.begin(), num.end());
   for(int i = 0; i < n-2; i++)
   {
      if (i > 0 && num[i-1] == num[i]) continue;
      int begin = i+1;
      int end = n - 1;
      while(begin < end)
      {
          int sum = num[i] + num[begin] + num[end];
          if(closest > abs(sum-target))
               result = sum, closest = abs(sum-target);
          if(sum > target)
              --end;
          else if (sum < target)
              ++begin;
          else
               return sum;         
       }
    }
   return move(result); 
}
```
 

