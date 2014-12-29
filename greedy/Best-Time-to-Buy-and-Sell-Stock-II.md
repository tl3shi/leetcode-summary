# Best Time to Buy and Sell Stock II

题目来源：[Best Time to Buy and Sell Stock II](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/)

>

    Say you have an array for which the ith element is the price of a given stock
    on day i.

    Design an algorithm to find the maximum profit. You may complete as many
    transactions as you like (ie, buy one and sell one share of the stock multiple
    times). However, you may not engage in multiple transactions at the same time
    (ie, you must sell the stock before you buy again).

解题思路：
这题目跟[前一题](./best-time-to-buy-and-sell-stock.html)的区别在于，这个题允许多次交易。

思路就是在一个递增序列里，最矮的点买进，最高的点卖出。这样得到的利润最大。于是算法就是找一段一段的递增序列。

```cpp
	
	int maxProfit(vector<int> &prices) 
    {
        int n = prices.size();
        if (n <= 1) return 0;
        int i = 0;
        int result = 0;
        while(i < n)
        {
            int j = i;
            while(j+1 < n && prices[j] <= prices[j+1])
                j++;
            if(j == n-1)
            {
                result += std::max(prices[n-1] - prices[i], 0);
                return result;
            };
            //prices[j]> prices[j+1]
            if(j > i)
                result += (prices[j] - prices[i]);
            i = std::max(i+1, j+1);
        }
        return result;
    }
```

后来看人家代码，才两三行，就觉得奇怪了。再分析下，举个例子，序列 1 3 4 5, 1进5出（一天只能交易一次）。相当于1进3出3进4出4进5出。于是就有了下面的代码。

```cpp
	
	int maxProfit(vector<int> &prices) 
    {
        int n = prices.size();
        int result = 0;
        for(int i = 1; i < n; i++)
            result += std::max(prices[i]-prices[i-1], 0);
        return result;
    }
```

