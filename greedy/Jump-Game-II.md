# Jump Game II

题目来源：[Jump Game II](https://oj.leetcode.com/problems/jump-game-ii/)

>
	Given an array of non-negative integers, you are initially positioned at the first index of the array.
	Each element in the array represents your maximum jump length at that position.
	Your goal is to reach the last index in the minimum number of jumps.
	For example:
	Given array A = [2,3,1,1,4]
	The minimum number of jumps to reach the last index is 2. (Jump 1 step from index 0 to 1, then 3 steps to the last index.)

解题思路：

跟 [jump-game](./jump-game.html)一样, 可以贪心。每次选择当前可以跳的范围内，下一次能跳得最远的 

```cpp
	
	int selectMaxIndex(int *A, int start, int range, int n)
    {
        int max_ = A[start];
        int max_index = start;
        int i = start+1;
        while(i < n && i <= start + range)
        {
            if(i + A[i] > max_)
            {
                max_ = i + A[i];
                max_index = i;
            }
            i++;
        }
        if(i >= n) return n;//goal achived
        return max_index;
    }
    int jump(int A[], int n) 
    {
        if(n == 0) return 0;
        int step = 0;
        int cur = 0;
        int goal = n - 1;
        while(cur < goal)
        {
            int range = A[cur];
            int next = selectMaxIndex(A, cur, range, n); ////每次选择当前可以跳的范围内，下一次能跳得最远的
            if(next <= cur) return -1;
            cur = next;
            ++step;
        }
        return step;
    }
```

学习下 [人家的](https://github.com/soulmachine/leetcode)代码就是简单.

```cpp
	
	int jump(int A[], int n) 
    {
        if(n == 0 || n == 1) return 0;
        int step = 0;
        int last = 0;
        int cur = 0;
        for(int i = 0;  i < n; i++)
        {
            if(i > last)
            {
                last = cur;
                ++step;
            }
            cur = std::max(cur, i + A[i]);
            if(cur >= n-1) return ++step;
            if(cur <= i) return -1;
        }
        return step;
    }
```

