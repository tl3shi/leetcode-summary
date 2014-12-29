# Binary Tree Level Order Traversal

题目来源：[Binary Tree Level Order Traversal](https://oj.leetcode.com/problems/binary-tree-level-order-traversal/)

>
	
	Given a binary tree, return the level order traversal of its nodes' values. (ie, from left to right, level by level).

	For example:
	Given binary tree {3,9,20,#,#,15,7},
	    3
	   / \
	  9  20
	    /  \
	   15   7
	return its level order traversal as:
	[
	  [3],
	  [9,20],
	  [15,7]
	]


解题思路：

###  常规方法, 两个queue交替

```cpp
	
	vector<vector<int> > levelOrder0(TreeNode *root)
	{
	    vector<vector<int> > result;
	    queue<TreeNode*> q1, q2;
	    q1.push(root);
	    while(! q1.empty())
	    {
	        vector<int> level;
	        while(!q1.empty())
	        {
	            auto node = q1.front(); q1.pop();
	            level.push_back(node->val);
	            if(node->left) q2.push(node->left);
	            if(node->right) q2.push(node->right);
	        }
	        std::swap(q1, q2);
	        result.push_back(level);
	    }
	    return move(result);
	}
```

###  单queue+隔板

前面[word ladder ii](./word-ladder-ii.html)就提到过bfs，用隔板将各层之间隔离出来。只用一个queue就能知道某层是否已经遍历完毕。

```cpp
	
	vector<vector<int> > levelOrder(TreeNode *root)
	{
	    vector<vector<int> > result;
	    queue<TreeNode*> q;
	    q.push(root);
	    TreeNode * split = nullptr;
	    while(! q.empty())
	    {
	        q.push(split);
	        vector<int> level;
	        while(q.front() != split)
	        {
	            auto node = q.front(); q.pop();
	            level.push_back(node->val);
	            if(node->left) q.push(node->left);
	            if(node->right) q.push(node->right);
	        }
	        result.push_back(level);
	        q.pop();//pop split;
	    }
	    return move(result);
	}
```

### 递归

递归写起来就是简单。

```cpp

	void levelOrderRecusion(TreeNode *root, int level, vector<vector<int> > &result)
    {
        if(level >= result.size())
            result.push_back(vector<int>());
        result[level].push_back(root->val);
        if(root->left)
            levelOrderRecusion(root->left, level+1, result);
        if(root->right)
            levelOrderRecusion(root->right, level+1, result);
    }
    vector<vector<int> > levelOrder(TreeNode *root) 
    {
        vector<vector<int> > result;
        if(root == NULL) return result;
        levelOrderRecusion(root, 0, result);
        return move(result);
    }
```

