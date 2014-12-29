# find minimum in rotated sorted array

题目来源：[Find Minimum in Rotated Sorted Array](https://oj.leetcode.com/problems/find-minimum-in-rotated-sorted-array/)

>
	Suppose a sorted array is rotated at some pivot unknown to you beforehand.
	(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).
	Find the minimum element.
	You may assume no duplicate exists in the array.

解题思路：

rotate总是至少有一半是有序的，可以根据这一半有序的值去二分。跟[Search in Rotated Sorted Array](./search-in-rotated-sorted-array.html)一样。

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
       }else if(num[left] <= num[mid]) //left is sorted, left maybe equals mid
       {
           result = std::min(result, num[left]);
           left = mid+1;
       }
   }
   return result;
}
```

