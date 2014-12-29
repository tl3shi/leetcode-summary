# Path Sum II

题目来源：[Path Sum II ](https://oj.leetcode.com/problems/path-sum-ii/)

>
	
	Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
	For example:
	Given the below binary tree and sum = 22,
	              5
	             / \
	            4   8
	           /   / \
	          11  13  4
	         /  \    / \
	        7    2  5   1
	return
	[
	   [5,4,11,2],
	   [5,8,4,5]
	]

解题思路：

跟[Path Sum](./path-sum.html)思路一样，不过这题把路径存起来。

```cpp
	
	void search(vector<int> &path, vector<vector<int> >&result, TreeNode* node, int target)
    {
        assert(node != NULL);
        int v = node->val;// Attention 0
        if(node->left == NULL && node->right == NULL)
        {
            if(target == v) 
            {
                path.push_back(v); //Attention 1
                result.push_back(path);
                path.pop_back();
            }
            return;
        }
        if(node->left)
        {
            path.push_back(v); //Attention 1
            search(path, result, node->left, target - v);
            path.pop_back();
        }
        if(node->right)
        {
            path.push_back(v); //Attention 1
            search(path, result, node->right, target - v);
            path.pop_back();
        }
    }
    vector<vector<int> > pathSum(TreeNode *root, int sum) 
    {
        vector<vector<int> > result;
        if(root == NULL) return result;
        vector<int> path;
        search(path, result, root, sum);
        return move(result);
    }
```

注意别被code中的表象所迷惑，将`//Attention 1`的代码提取到`//Attention 0`处。 path先后push_back会反映到递归调用里面去的。

不然应该下面这样写。

```cpp

	void search2(vector<int> &path, vector<vector<int> >&result, TreeNode* node, int target)
    {
        if(node == NULL) return;//cannot check if target is 0 then putinto result, for this result has been checked before invoke the recursion
        int v = node->val;
        path.push_back(v);
        if(node->left == NULL && node->right == NULL)
        {
            if(target == v) 
                result.push_back(path);
        }
        search2(path, result, node->left, target - v);
        search2(path, result, node->right, target - v);
        path.pop_back();
    }
```



