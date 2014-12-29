# Best Time to Buy and Sell Stock III

题目来源：[Best Time to Buy and Sell Stock III](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/)

>

    Say you have an array for which the ith element is the price of a given stock
    on day i.
    Design an algorithm to find the maximum profit. You may complete at most two
    transactions.
    Note:
    You may not engage in multiple transactions at the same time (ie, you must sell
    the stock before you buy again).

解题思路：

从[Best Time to Buy and Sell Stock](./best-time-to-buy-and-sell-stock.html)可知, 可以在O(n)的时间内，可以得到某个区间内的一次交易最大利润。设i从1到n-2，那么针对每一个i，看看在prices的子序列[0,...,i][i,...,n-1]上分别取得的最大利润即可，时间复杂度是O(n^2)。

```cpp
	
	int maxSub(vector<int> &prices, int start, int end)
    {
        vector<int> dp(end-start+1);
        dp[0] = 0;
        int min = prices[start];
        for(int i = start+1; i <= end; i++)
        {
            dp[i-start] = std::max(dp[i-start-1], prices[i]-min);
            min = std::min(min, prices[i]);
        }
        return dp[end-start];
    }
    
    int maxProfit(vector<int> &prices)
    {
        int n = prices.size();
        if(n <= 1) return 0;
        int result = 0;
        for(int i = 1; i < n-1; i++)
        {
            result = std::max(result,
                              maxSub(prices, 0, i) + maxSub(prices, i+1, n-1)
                              );
        }
        return result;
    }
```

可惜上面代码超时。

改进：那就是第一步扫描，先计算出子序列[0,...,i]中的最大利润，用一个数组保存下来，那么时间是O(n)。第二步是逆向扫描，计算子序列[i,...,n-1]上的最大利润，这一步同时就能结合上一步的结果计算最终的最大利润了，这一步也是O(n)。[ref Here](http://blog.unieagle.net/2012/12/05/leetcode%E9%A2%98%E7%9B%AE%EF%BC%9Abest-time-to-buy-and-sell-stock-iii%EF%BC%8C%E4%B8%80%E7%BB%B4%E5%8A%A8%E6%80%81%E8%A7%84%E5%88%92/)
另外，[此类问题这里有分析](http://www.cnblogs.com/TenosDoIt/p/3436457.html).

```cpp
	
	int maxProfit2(vector<int> &prices)
    {
        int n = prices.size();
        if(n <= 1) return 0;
        int result = 0;
        vector<int> head(n, 0);
        vector<int> tail(n, 0);
        head[0] = 0;
        int min = prices[0];
        for(int i = 1; i < n; i++)
        {
            head[i] = std::max(head[i-1], prices[i]-min);
            min = std::min(min, prices[i]);
        }
        tail[n-1] = 0;//tail[i], [i:n-1]
        int max = prices[n-1];
        for(int i = n-2; i >=0; i--)
        {
            tail[i] = std::max(tail[i+1], max-prices[i]);
            max = std::max(max, prices[i]);
        }
        for(int i = 0; i < n; i++)
            result = std::max(result, head[i] + tail[i]);
        return result;
    }
```

