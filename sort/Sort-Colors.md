# Sort Colors

题目来源：[Sort Colors](https://oj.leetcode.com/problems/sort-colors/)

>
	Given an array with n objects colored red, white or blue, sort them so that objects of the same color are adjacent, with the colors in the order red, white and blue.
	Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.	
	Note:
	You are not suppose to use the library's sort function for this problem.
	A rather straight forward solution is a two-pass algorithm using counting sort.
	First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
	Could you come up with an one-pass algorithm using only constant space?

解题思路：
	

###  countSort= O(2\*n)

按照提示，分别数数0,1,2各有多少个，然后填充进去即可。简单的countsort.

```cpp
	
	void sortColors(int A[], int n) 
    {
        int one = 0, two = 0, zero = 0;
        for(int i = 0; i < n; i++)
        {
            if(A[i] == 0)
                ++zero;
            else if(A[i] == 1)
                ++one;
            else
                ++two;
        }
        int i = 0;
        while(i < zero)
            A[i++] = 0;
        while(i < zero+one)
            A[i++] = 1;
        while(i < zero+one+two)
            A[i++] = 2;
    }
```

###  O(1\*n) 算法

设前面的数字已经排好序.  0000 111 222 *1\*02*… 

记录第一次出现1的index，第一次出现2的index， 当前搜索的数是1的话，将first2改为1，当前index的数改为2即可...即:

	current = 1: first2 = 1, current=2; 
	current = 0: first1=0,first2=1,current=2; 
	current = 2: continue即可。 
	
注意修改方式从后往前即可避免繁琐的边界值(first2=first1等情况) 
这个主要是参考了[anyone with one pass and constant space solution](https://oj.leetcode.com/discuss/1827/anyone-with-one-pass-and-constant-space-solution).

```cpp
	
	 void sortColors(int A[], int n) 
    {
        if(n <= 1) return;
        int zero = 0;
        int one = 0;
        int two = 0;
        for(int cur = 0; cur < n; cur++)
        {
            if(A[cur] == 2){
                A[two++]=2;
            }else if(A[cur] == 1){
                A[two++]=2;
                A[one++]=1;
            }else{ //0
                A[two++]=2;
                A[one++]=1;
                A[zero++]=0;
            }
        }
    }
```

###  O(1\*n) 算法

双指针算法, 参考 [leetcode-cpp](https://github.com/soulmachine/leetcode).

	zero记录最后一个0的的后一个index(可能是1或2), two记录最开始一个2的位置。
	cur == 0: 将zero的后一个与cur交换, 二者都+1;
	cur == 2: 将two和当前对应值交换, two是放2的位置，下一次放2,放到two-1的地方, 交换的值可能是0，所以cur的指针不能后移。`1 2(cur) 0`, 2与0交换后, 0还得与前面的1交换。

```cpp

	void sortColors(int A[], int n) 
    {
        if(n <= 1) return;
        int zero = 0; int two = n-1;
        int i = 0;
        while(i <= two)
        {
            if(A[i] == 0)
                std::swap(A[zero++], A[i++]);
            else if(A[i] == 2)
                std::swap(A[two--], A[i]);//i cannot ++, maybe A[two] is zero.
            else
                i++;
        }
    }
```

