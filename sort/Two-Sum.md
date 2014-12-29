# Two Sum


题目来源:[leetcode-two-sum](https://oj.leetcode.com/problems/two-sum/)

>
	Given an array of integers, find two numbers such that they add up to a specific target number.
	The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2. Please note that your returned answers (both index1 and index2) are not zero-based.
	You may assume that each input would have exactly one solution.
	Input: numbers={2, 7, 11, 15}, target=9
	Output: index1=1, index2=2


解答：

1、先排序（得记录index），i->0, j->n 相加结果sum<target, i++ 否则 j—

```cpp

vector<int> twoSum(vector<int> &numbers, int target)
{ 
    vector<pair<int, int> > num_index_map;
    for(int i = 0; i < numbers.size(); i++)
        num_index_map.push_back(pair<int, int>(numbers[i], i+1));
    std::sort(num_index_map.begin(), num_index_map.end(), [](const pair<int,int> &a, const pair<int,int> &b){return a.first < b.first;} );
    int i = 0;
    int j = numbers.size() - 1;
    while(i < j)
    {
        int tmp = num_index_map[i].first + num_index_map[j].first;
        if( tmp == target)
        {
            vector<int> result(2); //capacity, then push back, becomes 3
            //quick sort is not stable.
            if(num_index_map[i].second < num_index_map[j].second)
            {
                result[0] = (num_index_map[i].second);
                result[1] = (num_index_map[j].second);
            }else
            {
                result[1] = (num_index_map[i].second);
                result[0] = (num_index_map[j].second);
            }
            return result;
        }else if(tmp < target)
        {
            i++;
        }else
        {
            j--;
        }
    }
    return vector<int>();
}
```

2、用map存起来～直接找对应的另一半
	
```cpp

	vector< int> twoSum(vector< int > &numbers, int target)
	{
	    unordered_map< int , int > numIndex;
	    int index = 0;
	    for( auto num : numbers)
	    {
	        if (numIndex.find(target - num) != numIndex.end())
	        {
	            return vector<int >{numIndex[target-num]+1, index+1};
	        }
	        numIndex[num] = index++;
	    }
	}
```

