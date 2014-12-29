# Binary Tree Maximum Path Sum

题目来源：[Binary Tree Maximum Path Sum](https://oj.leetcode.com/problems/binary-tree-maximum-path-sum/)

>

    Given a binary tree, find the maximum path sum.
    The path may start and end at any node in the tree.
    For example:
    Given the below binary tree,
      1
     / \
    2   3
    Return 6.

解题思路：

path路径能以任意节点开头或结尾。注意maxPathSum(root) != max{ maxPathSum(root.left), maxPathSum(root.right), maxPathSum(root.left) + maxPathSum(root.right) + root.val }， 右/左 子树的最大结果很有可能不能跟当前节点连在一起。

```cpp
	
	// ended/started with root, the max path
	int subMax(TreeNode *root, int &global_max)
	{
	    if(root == NULL) return 0;
	    int l_max = 0;
	    int r_max = 0;
	    l_max = std::max(subMax(root->left, global_max), 0); //if 0, not choose left child
	    r_max = std::max(subMax(root->right, global_max), 0);
	    int max_ = root->val + l_max + r_max; //global_max: connected current node
	    if(global_max < max_)
	        global_max = max_;
	    return std::max(0, std::max(l_max, r_max) + root->val);
	}
	//Attention, for the max(root.right) may not connected with root
	//maxPathSum(root) != max{ maxPathSum(root.left), maxPathSum(root.right), maxPathSum(root.left) + maxPathSum(root.right) + root.val }
	
	int maxPathSum(TreeNode *root)
	{
	    int global_max = INT_MIN;
	    subMax(root, global_max);
	    return global_max;
	}
```

