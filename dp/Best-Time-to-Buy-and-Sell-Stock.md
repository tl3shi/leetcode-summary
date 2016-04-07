# Best Time to Buy and Sell Stock

题目来源：[Best Time to Buy and Sell Stock](https://oj.leetcode.com/problems/best-time-to-buy-and-sell-stock/)

>

    Say you have an array for which the ith element is the price of a given stock
    on day i.
    If you were only permitted to complete at most one transaction (ie, buy one and
    sell one share of the stock), design an algorithm to find the maximum profit.

解题思路：

最简单就是O(n^2)暴力解法，可惜超时，过不了。
用DP, dp[i]表示前i个的最大利润。

```cpp
	
	int maxProfit(vector<int> &prices) 
    {
        int n = prices.size();
        if(n <= 1) return 0;
        vector<int> dp(n, 0);
        int min_ = prices[0];
        for(int i = 1; i < n; i++)
        {
            dp[i] = std::max(dp[i-1], prices[i]-min_);
            min_ = std::min(min_, prices[i]);
        }
        return dp[n-1];
    }
```


