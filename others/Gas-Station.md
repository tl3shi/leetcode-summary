# Gas Station

题目来源：[Gas Station](https://oj.leetcode.com/problems/gas-station/)

>

    There are N gas stations along a circular route, where the amount of gas at
    station i is gas[i].

    You have a car with an unlimited gas tank and it costs cost[i] of gas to travel
    from station i to its next station (i+1). You begin the journey with an empty
    tank at one of the gas stations.

    Return the starting gas station's index if you can travel around the circuit
    once, otherwise return -1.

    Note:
    The solution is guaranteed to be unique.

解题思路：

###  暴力法

一个一个试～  `O(N^2)` 能AC。

```cpp
	
	bool ok(vector<int> &gas, vector<int> &cost, int startIndex)
    {
        int n = gas.size();
        int i = 0;
        int remain = 0;
        int index = startIndex;
        while(i < n)
        {
            if (remain + gas[index] - cost[index] < 0)
                return false;
            remain += gas[index] - cost[index];
            i++;
            index  = (index+1)%n;
        }
        if(i == n) return true;
    }
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost) 
    {
        int n = gas.size();
        for(int i = 0; i  < n; i++)
        {
            if(ok(gas, cost, i))
                return i;
        }
        return -1;
    }
```

###  O(N)解法

从[discuss](https://oj.leetcode.com/discuss/4159/share-some-of-my-ideas)看来的答案。思路如下：

>
	1. If car starts at A and can not reach B. Any station between A and B can not reach B.(B is the first station that A can not reach.)
	2. If the total number of gas is bigger than the total number of cost. There must be a solution.
	3. Every time a fail happens, accumulate the amount of gas that is needed to overcome the fail. After looping through the stations, if the gas left is more than gas needed, then we have a solution, otherwise not.

```cpp
	
	 int canCompleteCircuit(vector<int> &gas, vector<int> &cost) 
    {
        int n = gas.size();
        int remain = 0;
        int sum = 0;
        int start = 0;
        for(int i = 0; i < n; i++)
        {
            if (remain + gas[i] - cost[i] < 0)
            {
                start = i+1;
                remain = 0;
            }else
                remain += gas[i] - cost[i];
            sum += gas[i] - cost[i];
        }
        return sum >= 0 ? start : -1;
    }
```

