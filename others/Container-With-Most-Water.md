# Container With Most Water

题目来源：[Container With Most Water](https://oj.leetcode.com/problems/container-with-most-water/)

>
	Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
	Note: You may not slant the container

解题思路：

从 [discuss](https://oj.leetcode.com/discuss/1074/anyone-who-has-a-o-n-algorithm) 得到的答案。

```cpp
	
	int maxArea(vector<int> &height) 
    {
        if(height.size() == 0) return 0;
        int result = 0;
        int left = 0;
        int right = height.size() - 1;
        while(left < right)
        {
            result = std::max(result, (right-left) * std::min(height[left], height[right]));
            if(height[left] < height[right])
                ++left;
            else
                --right;
        }
        return result;
    }
```

怎么证明是对的?

>
Suppose the returned result is not the optimal solution. Then there must exist an optimal solution, say a container with aol and aor (left and right respectively), such that it has a greater volume than the one we got. Since our algorithm stops only if the two pointers meet. So, we must have visited one of them but not the other. WLOG, let's say we visited aol but not aor. When a pointer stops at a_ol, it won't move until
>
   * The other pointer also points to aol. In this case, iteration ends. But the other pointer must have visited aor on its way from right end to aol. Contradiction to our assumption that we didn't visit aor.
   * The other pointer arrives at a value, say arr, that is greater than aol before it reaches aor. In this case, we does move aol. But notice that the volume of aol and arr is already greater than aol and aor (as it is wider and heigher), which means that aol and aor is not the optimal solution -- Contradiction!

或者

v[low, high] 表示(low, hight)和x轴围成的容器装水的结果，假设height[low] < height[high]，那么算法将low++, 这意味着v[low, high-1],v[low, high-2]等被忽略。v[low, high-1],v[low, high-2]…...不会大于v[low, high]，因为装水的容量是由宽度和短的那个height[low]决定的(low是固定的)，宽度显然(low, high)更宽。

