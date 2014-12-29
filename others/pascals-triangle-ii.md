# Pascal's Triangle II

题目来源：[Pascal's Triangle II](https://oj.leetcode.com/problems/pascals-triangle-ii/)

>

    Given an index k, return the kth row of the Pascal's triangle.
    For example, given k = 3,
    Return [1,3,3,1].
    Note:
    Could you optimize your algorithm to use only O(k) extra space?

解题思路：

二项式系数求法。

```cpp
	
	int C(int n, int k)
    {
        if(n-k < k) return C(n, n-k);
        //C(7,3)=
        //7*6*5 / 1*2*3
        long long result = 1;//int may overflow
        for(int i = 0; i < k; i++)
            result= result*(n-i)/(i+1);
        return (int)result;//including k == 0
    }
    vector<int> getRow(int n) 
    {
        int mid = (n >> 1)+1;//3->2: [0,1]  4->3:[0,2]
        vector<int> result(n+1, 1);
        for(int i = 0; i < mid; i++)
        {
            result[i] = C(n, i);
            result[n-i]= result[i];
        }
        return move(result);    
    }
```


