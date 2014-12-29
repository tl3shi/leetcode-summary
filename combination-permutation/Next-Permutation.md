# Next Permutation

题目来源：[Next Permutation](https://oj.leetcode.com/problems/next-permutation/)

>
	Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
	If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
	The replacement must be in-place, do not allocate extra memory.
	Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
	1,2,3 → 1,3,2
	3,2,1 → 1,2,3
	1,1,5 → 1,5,1

解题思路：

这里 [permutations-ii](./permutations-ii.html)其实已经实现过一次了。

```cpp
	
	void nextPermutation(vector<int> &num) 
    {
        int n = num.size();
        int index = n - 1;//2 [3] 5 4 1
        while(index-1 >= 0 && num[index-1] >= num[index])  
            --index;
        if(index == 0)
        {
            std::reverse(num.begin(), num.end());
            return;
        }
        --index; //[3]
        int bigger = n-1; //find[4]
        while(bigger != index && num[bigger] <= num[index])
            --bigger;
        std::swap(num[index], num[bigger]);
        std::reverse(num.begin()+index+1, num.end());
    }
```

