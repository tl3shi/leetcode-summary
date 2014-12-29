# First Missing Positive

题目来源：[First Missing Positive](https://oj.leetcode.com/problems/first-missing-positive/)

>
	Given an unsorted integer array, find the first missing positive integer.
	For example,
	Given [1,2,0] return 3,
	and [3,4,-1,1] return 2.
	Your algorithm should run in O(n) time and uses constant space.

解题思路：

注意有可能含有重复的，若非重复的可以用应该得的正数和和实际正数和之差得到miss的正数，如果为0的话，就是本来就是连续的数，first missing的就是max+1. 含有重复的话可以用 

这里用原地改变下数组的位置来算，例如 3 3 1 4 0,将index所在的数（[0,n]的数）放到应该放的数里面去（数-1），比如这里应该是放到 3 应该放到index＝2，1放到index＝0，4放到index＝3，所有数的放好后，再从头开始扫描数组，第一个下标所得的数不是index+1，那么差的就是这个数。复杂度不超过O（2*n） 
A里面的数，若A[i]是正数0-n之间的，则把TA放到位置i-1处。即最后达到的效果是 A[i]=i+1，不然就是负数 或者大于n的数。第一遍遍历把所有的数归位，第二遍找，哪个位置差了，就那个位置对应的数i+1就是差的正数。


第一版本的代码确实很戳啊。

```cpp

	int firstMissingPositive(int A[], int n)
	{
	    if (n == 0) return 1;
	    if (n == 1) return A[0] > 0 ? (A[0] == 1 ? 2 : 1) : 1;
	    
	    int index = 0;
	    while(index < n)
	    {
	        int tmp = A[index];
	        bool goon = true;
	        while(goon)
	        {
	            if(tmp-1 >=0 && tmp-1 < n)
	            {
	                if(A[tmp-1] == tmp)
	                {
	                    goon = false;
	                    index++;
	                }
	                else
	                {
	                    int tmpbak = A[tmp-1];
	                    A[tmp-1] = tmp;
	                    tmp = tmpbak;
	                }
	            }else
	            {
	                break;
	            }
	        }
	        while(index < n && (A[index] == index+1 ||
	              A[index] <= 0 || A[index] >= n))
	            index++;
	    }
	    
	    index = 0;
	    while(index < n)
	    {
	        if(A[index] != index+1)
	            return index+1;
	        index++;
	    }
	    return n+1;
	}
```

其实跟下面的代码一个意思。

```cpp
	
	int firstMissingPositive(int A[], int n) 
    {
        if(n == 0) return 1;
        int i = 0;
        while(i < n)
        {
            while(i < n && A[i] != i+1)
            {
                if(A[i] <= 0 || A[i] > n || A[i] == A[A[i]-1])
                    i++;
                else
                    std::swap(A[i], A[A[i]-1]);
            }
            i++;
        }
        for(int i = 0; i < n; i++)
            if(A[i] != (i+1)) return i+1;
        return n+1;
    }
```

