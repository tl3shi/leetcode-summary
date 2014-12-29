# Merge Intervals

题目来源：[Merge Intervals](https://oj.leetcode.com/problems/merge-intervals/)

>
	Given a collection of intervals, merge all overlapping intervals.
	For example,
	Given [1,3],[2,6],[8,10],[15,18],
	return [1,6],[8,10],[15,18].
	
解题思路：

先对start排序, 排序时这样 
[1,4] [1,5]时,[1,5][1,4]  统一处理[1,4][2,4]吃掉。 
然后数轴上对前后两个interval作讨论，3种情况，一种including，i+1包含在i里面; i+1和i相交，i+1和i相隔。 

```cpp

	/**
	 * Definition for an interval.
	 * struct Interval {
	 *     int start;
	 *     int end;
	 *     Interval() : start(0), end(0) {}
	 *     Interval(int s, int e) : start(s), end(e) {}
	 * };
	 */
	int cmp(const Interval &i1, const Interval &i2)
	{
	    if(i1.start == i2.start) return i1.end > i2.end; // make second bigger first
	    return i1.start < i2.start;
	}
	class Solution 
	{
	public:
	    vector<Interval> merge(vector<Interval> &intervals)
	    {
	        vector<Interval> result;
	        if(intervals.size() <= 1) return intervals;
	        std::sort(intervals.begin(), intervals.end(), cmp);
	        int i = 1;
	        auto start = intervals[0];
	        while(i < intervals.size())
	        {
	            if(intervals[i].end <= start.end)
	            {
	                i++;
	            }else if(intervals[i].start <= start.end && intervals[i].end >= start.end)
	            {
	                start.end = intervals[i].end;
	                i++;
	            }
	            else
	            {
	                result.push_back(start);
	                if(i < intervals.size())
	                    start = intervals[i];
	                else
	                    return result;
	            }
	        }
	        result.push_back(start);
	        return move(result);
	    }
	};
```

当然，也可以借助 [Insert Interval](./Insert-Interval.html) 一个一个插入到结果里面去。

```cpp

	vector<Interval> merge(vector<Interval> &intervals)
	{
	    vector<Interval> result;
	    if(intervals.size() <= 1) return intervals;
	    for(int i = 0; i < intervals.size(); i++)
	        result = insert(result, intervals[i]);
	    return move(result);
	}
	vector<Interval> insert(vector<Interval> &intervals, Interval newInterval)
	{
	    if(intervals.size() == 0) return vector<Interval>(1, newInterval);
	    int n = intervals.size();
	    vector<Interval> result;
	    for(int i = 0; i < n; i++)
	    {
	        auto &it = intervals[i];
	        if(newInterval.end < it.start)
	        {
	            result.push_back(newInterval);
	            std::copy(intervals.begin()+i, intervals.end(), std::back_inserter(result));
	            return move(result);
	        }else if(newInterval.start > it.end)
	            result.push_back(it);
	        else
	        {
	            newInterval.start = std::min(newInterval.start, it.start);
	            newInterval.end = std::max(newInterval.end, it.end);
	        }
	    }
	    result.push_back(newInterval);
	    return move(result);
	}
```
 

