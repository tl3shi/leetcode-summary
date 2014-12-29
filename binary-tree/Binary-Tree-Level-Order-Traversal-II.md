# Binary Tree Level Order Traversal II

题目来源：[Binary Tree Level Order Traversal
II](https://oj.leetcode.com/problems/binary-tree-level-order-traversal-ii/)

>
	
	Given a binary tree, return the bottom-up level order traversal of its nodes' values. (ie, from left to right, level by level from leaf to root).

	For example:
	Given binary tree {3,9,20,#,#,15,7},
	    3
	   / \
	  9  20
	    /  \
	   15   7
	return its bottom-up level order traversal as:
	[
	  [15,7],
	  [9,20],
	  [3]
	]


解题思路：

跟前一题[Binary Tree Level Order Traversal](./binary-tree-level-order-traversal.html)唯一的区别就是这个将最后结果reverse一下。
这里就只列了其中一种代码了。

###  常规方法, 两个queue交替

参见[Binary Tree Level Order Traversal](./binary-tree-level-order-traversal.html)。
 

###  单queue+隔板

前面[word ladder ii](./word-ladder-ii.html)就提到过bfs，用隔板将各层之间隔离出来。只用一个queue就能知道某层是否已经遍历完毕。

```cpp
	
	 vector<vector<int> > levelOrderBottom(TreeNode *root) 
    {
        vector<vector<int> > result;
        if(root == NULL) return result;
        queue<TreeNode*> q;
        q.push(root);
        while(! q.empty())
        {
            q.push(NULL);
            vector<int> level;
            while(q.front() != NULL)
            {
                auto node = q.front(); q.pop();
                level.push_back(node->val);
                if(node->left) q.push(node->left);
                if(node->right) q.push(node->right);
            }
            result.push_back(level);
            q.pop();//pop NULL
        }
        std::reverse(result.begin(), result.end());
        return move(result);
    }
```

### 递归

参见[Binary Tree Level Order Traversal](./binary-tree-level-order-traversal.html)。
 

