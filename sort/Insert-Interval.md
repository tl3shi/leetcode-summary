# Insert Interval

题目来源：[Insert Interval](https://oj.leetcode.com/problems/insert-interval/)

>

	Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).You may assume that the intervals were initially sorted according to their start times.
	Example 1:
	Given intervals [1,3],[6,9], insert and merge [2,5] in as [1,5],[6,9].
	Example 2:
	Given [1,2],[3,5],[6,7],[8,10],[12,16], insert and merge [4,9] in as [1,2],[3,10],[12,16]. This is because the new interval [4,9] overlaps with [3,5],[6,7],[8,10].

解题思路：

可以先加进去，然后再按照[Merge Intervals](./Merge-Intervals.html)的算法merge一下就行。

```cpp
	
	vector<Interval> merge2(vector<Interval> &intervals)
    {
        vector<Interval> result;
        if(intervals.size() == 1) return intervals;
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
    vector<Interval> insert(vector<Interval> &intervals, Interval newInterval)
    {
        if(intervals.size() == 0) return vector<Interval>(1, newInterval);
         int i = 0;
        vector<Interval> newIntervals(intervals.size()+1);
         
        while(i < intervals.size())
        {
            if(intervals[i].start < newInterval.start)
            {
                i++;
            }else if (intervals[i].start == newInterval.start)
            {
                if(intervals[i].end >= newInterval.end)
                    ;
                else
                    i++; //the newInterval first
                break;
            }else
            {
                break;
            }
        }
        int index = 0;
        while(index < i)
        {
            newIntervals[index] = intervals[index];
            index++;
        }
        newIntervals[index] = newInterval;
        while(index < intervals.size())
        {
            newIntervals[index+1] = intervals[index];
            index++;
        }
        return merge2(newIntervals);
    }
```


或者 直接加。参考了 [leetcode-cpp](https://github.com/soulmachine/leetcode)
原文中的代码貌似有个testcase 过不了TLE。

```cpp
	
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

