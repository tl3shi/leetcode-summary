# Candy

题目来源：[Candy](https://oj.leetcode.com/problems/candy/)

>

    There are N children standing in a line. Each child is assigned a rating value.

    You are giving candies to these children subjected to the following
    requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.
    What is the minimum candies you must give?

解题思路：


解析：注意理解题意 [3,2,2,3,1] 糖数量: 2,1,1,2,1; [4,2,3,4,1] 结果是 2,1,2,3,1. 

###  每次找最低点，再往回确定糖数量

遍历一两遍即可,每次找下一次最低点，最低点的糖数量为1，再从最低的遍历到当前点得到结果。下面代码用了一个数组保存了每个child的结果，实际上只需用几个变量记录即可。
按照这个思路写了下面的比较戳的代码。

```cpp

	//nextLowest and max index
	int nextLowest(vector<int> &ratings, int startIndex)
	{
	    if(startIndex == ratings.size() - 1) return startIndex;
	    while(ratings[startIndex] >= ratings[startIndex+1])
	    {
	        startIndex++;
	        if(startIndex == ratings.size() - 1)
	            return startIndex;
	    }
	    return startIndex;
	}
	
	//use two other variables to store candies[index-1] candies[index+1]
	//can change the space complexity to O(1)
	int candy(vector<int> &ratings)
	{
	    size_t len = ratings.size();
	    if(len <= 1) return (int)len;
	    int curIndex = 0;
	    int nextLow = nextLowest(ratings, curIndex);
	    int sum = 0;
	    vector<int> candies(len);
	    while(curIndex < len)
	    {
	        if(curIndex == nextLow)
	        {
	            if(curIndex == 0)
	                candies[curIndex] = 1;
	            else
	                candies[curIndex] = candies[curIndex-1] + 1;
	            sum += candies[curIndex];
	        }else
	        {
	            int index = nextLow;
	            while(index-1 >= curIndex)
	            {
	                if(ratings[index-1] == ratings[index])
	                {
	                    if(index+1 <= nextLow && ratings[index] > ratings[index+1])
	                        candies[index] = candies[index+1] + 1;
	                    else
	                        candies[index] = 1;
	                    sum += candies[index];
	                }else // ratings[index-1] > ratings[index]
	                {
	                    if(index == nextLow || (index+1 <= nextLow && ratings[index] == ratings[index+1]))
	                        candies[index] = 1;
	                    else
	                        candies[index] = candies[index+1] + 1;
	                    sum += candies[index];
	                }
	                --index;
	                if(index == curIndex)
	                {
	                    //4 2 3 [4] 1
	                    if(ratings[index] > ratings[index+1] && (index-1 >= 0 && ratings[index] > ratings[index-1]) )
	                        candies[index] = std::max(candies[index+1], candies[index-1]) + 1;
	                    else if(ratings[index] > ratings[index+1])
	                        candies[index] = candies[index+1] + 1;
	                    else if(ratings[index] > ratings[index-1])
	                        candies[index] = candies[index-1] + 1; //1 [2] 2
	                    else
	                        candies[index] = 1;
	                    sum += candies[index];
	                    break;
	                }
	            }
	        }
	        curIndex = nextLow+1;
	        nextLow = nextLowest(ratings, curIndex);
	    }
	    return sum;
	}
```


###  从左到右从右到左双向遍历

从[discuss](https://oj.leetcode.com/discuss/76/does-anyone-have-a-better-idea)看到的答案，短小精悍的代码。思路也很清晰。

>
	1. From left to right, to make all candies satisfy the condition if ratings[i] > ratings[i - 1] then candies[i] > candies[i - 1], just ignore the right neighbor as this moment. We can assume leftCandies[i] is a solution which is satisfied.
	2. From right to left, almost like step 1, get a solution rightCandies[i] which just satisfy the condition if ratings[i] > ratings[i + 1] then candies[i] > candies[i + 1]
	3. For now, we have leftCandies[i] and rightCandies[i], so how can we satisfy the real condition in the problem? Just make candies[i] equals the maximum betweenleftCanides[i] and rightCandies[i]
	
即把整个过程分为两个步骤，第一步从左到右，只要右边的ratings大于自己，右边的糖数量就＝自己+1, (先不管左边大于右边的情况)，这一步完成之后有条件,`ratings[i] > ratings[i - 1] && candies[i] > candies[i - 1]` 然后再从右往左，一样的思路，使得`ratings[i] > ratings[i + 1] && candies[i] > candies[i + 1]`。 最后candies再取两个中的max，这样就同时满足这两个条件。问题解决。

```cpp

	int candy2(vector<int> &ratings)
	{
	    int n = ratings.size();
	    if(n <= 1) return n;
	    vector<int> candies(n, 1);
	    //left to right
	    for(int i = 1; i < n; i++)
	    {
	        if(ratings[i] > ratings[i-1])
	            candies[i] = candies[i-1]+1;
	        else
	            candies[i] = 1;
	    }
	    int total = candies[n-1];
	    for(int i = n-2; i >= 0; i--)
	    {
	        if(ratings[i] > ratings[i+1])
	            candies[i] = std::max(candies[i+1]+1, candies[i]);
	        total += candies[i];
	    }
	    return total;
	}

```

###  备忘录法

这个方法参考了[leetcode-cpp](https://github.com/soulmachine/leetcode)。即用递归的方式使得分得candy数量同时满足以上两个条件。

```cpp

	int f(vector<int> &ratings, vector<int> &cache, int index){
	    if(cache[index] == 0)//has not been calculated before
	    {
	        cache[index] = 1;
	        if(index+1 < ratings.size() && ratings[index] > ratings[index+1])
	            cache[index] = std::max(cache[index], f(ratings, cache, index+1)+1);
	        if(index-1 >= 0 && ratings[index] > ratings[index-1])
	            cache[index] = std::max(cache[index], f(ratings, cache, index-1)+1);
	    }
	    return cache[index];}
	int candy3(vector<int> &ratings){
	    int n = ratings.size();
	    if(n <= 1) return n;
	    int total = 0;
	    vector<int> cache(n, 0);
	    for(int i = 0; i < n; i++)
	        total += f(ratings, cache, i);
	    return total;
	}
```

