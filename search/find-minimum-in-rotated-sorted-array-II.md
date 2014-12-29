# find minimum in rotated sorted array II

题目来源：[Find Minimum in Rotated Sorted Array II](https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/)

>
	Follow up for "Find Minimum in Rotated Sorted Array":
	What if duplicates are allowed?
	Would this affect the run-time complexity? How and why? Suppose a sorted array is rotated at some pivot unknown to you beforehand.
	(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
	Find the minimum element.
	The array may contain duplicates.

解题思路：

跟[Search in Rotated Sorted Array II](./search-in-rotated-sorted-array-ii.html)一样。

```cpp
int findMin(vector<int> &num) 
{
   assert(num.size() != 0);
   if(num.size() == 1) return num[0];
   int result = INT_MAX;
   int left = 0; int right = num.size() - 1;
   while(left <= right)
   {
       int mid = left + ((right - left)>>1);
       if (num[mid] < num[right])//right is sorted
       {
           result = std::min(result, num[mid]);
           right = mid-1;
       }else if(num[left] < num[mid]) //left is sorted
       {
           result = std::min(result, num[left]);
           left = mid+1;
       }else if(num[mid] == num[left])
           ++left, result = std::min(result, num[mid]);
       else
           --right, result = std::min(result, num[mid]);
   }
   return result;    
}
```

