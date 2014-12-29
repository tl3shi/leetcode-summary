# Maximum Depth of Binary Tree

题目来源：[Maximum Depth of Binary Tree ](https://oj.leetcode.com/problems/maximum-depth-of-binary-tree/)

>

	Given a binary tree, find its maximum depth.
	The maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

解题思路：

跟[Minimum Depth of Binary Tree](https://oj.leetcode.com/problems/minimum-depth-of-binary-tree/)思路一样，这个更简答。

```cpp
	
	int depth(TreeNode* root){
        if(root->left == NULL && root->right == NULL) return 1;
        int left = 0; int right = 0;
        if(root->left) left = depth(root->left);
        if(root->right) right = depth(root->right);
        return std::max(left, right) + 1;
    }
    int maxDepth(TreeNode *root) 
    {
        if(root == NULL) return 0;
        return depth(root);
    }
```

