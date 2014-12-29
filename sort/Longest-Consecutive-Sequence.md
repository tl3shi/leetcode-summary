# Longest Consecutive Sequence

题目来源：[Longest Consecutive Sequence](https://oj.leetcode.com/problems/longest-consecutive-sequence/)

>

    Given an unsorted array of integers, find the length of the longest consecutive
    elements sequence.

    For example,
    Given [100, 4, 200, 1, 3, 2],
    The longest consecutive elements sequence is [1, 2, 3, 4]. Return its length:
    4.

    Your algorithm should run in O(n) complexity.

解题思路：

###  利用hashmap

用一个set/map记录每个数，然后挨个找相邻的数字，每找到一个就从原set/map中去掉，直到全部遍历完毕。

```cpp

	int longestConsecutive(vector<int> &num)
	{
	    int result = 0;
	    unordered_set<int> data(num.begin(), num.end());
	    while(! data.empty())
	    {
	        int v = *(data.begin());
	        data.erase(data.begin());
	        int i = 1;
	        int len = 1;
	        while(data.find(v-i) != data.end())
	        {
	            ++len;
	            data.erase(data.find(v-i));
	            ++i;
	        }
	        i = 1;
	        while(data.find(v+i) != data.end())
	        {
	            ++len;
	            data.erase(data.find(v+i));
	            ++i;
	        }
	        result = std::max(result, len);
	    }
	    return result;
	}
```

###  先利用O(n)的排序

这也是参考了[discuss](https://oj.leetcode.com/discuss/2731/this-problem-has-a-o-n-solution?show=4368#a4368)的答案。 先用一个O(n)的排序算法，然后挨个左右看就是。
注意数组中可能含有相同的数字以及负数。

这里用基数排序radixsort，注意基数排序中内部计数排序时注意，输入可能含有负数，因此映射的下标不能是[0,9],而是还得把负数的另外一半算上即[0,18],-9->0, 9->18.

```cpp
	
	//-9 ---> index is 0 //9 --->index is 18
	int getBucket(int n, int base)
	{
	    return n / base % 10 + 9;
	}
	
	//按照个位(base=1)、十位(base=10)排序
	void countSort(vector<int> &num, int base)
	{
	    vector<int> numback(num);
	    vector<int> counts(19, 0);
	    for(int i = 0; i < numback.size(); i++)
	    {
	        int bucket = getBucket(numback[i], base);
	        ++counts[bucket];
	    }
	    for(int j = 1; j < counts.size(); j++)
	        counts[j] += counts[j-1];
	    for(int j = (int)numback.size()-1; j >= 0; j--)
	    {
	        int index = getBucket(numback[j], base);
	        num[counts[index]-1] = numback[j];
	        counts[index]--;
	    }
	}
	//O(N) sort, then scan to get the result
	void radixSort(vector<int> &num)
	{
	    int max = INT_MIN;
	    for(int i = 0; i < num.size(); i++)
	        max = std::max(max, abs(num[i])); //!! abs
	    int base = 1;
	    while(max / base)
	    {
	        countSort(num, base);
	        base *= 10;
	    }
	}
	//ref https://oj.leetcode.com/discuss/2731/this-problem-has-a-o-n-solution?show=4368#a4368
	int longestConsecutive2(vector<int> &num)
	{
	    if(num.size() <= 1) return num.size();
	    radixSort(num);
	    int max = 1;
	    int len = 1;
	    for(int i = 1; i < num.size(); i++)
	    {
	        if(num[i] == num[i-1])//!!
	            continue;
	        if(num[i] == num[i-1] + 1)
	            len++;
	        else
	        {
	            max = std::max(max, len);
	            len = 1;
	        }
	    }
	    return std::max(max, len);
	}

```

