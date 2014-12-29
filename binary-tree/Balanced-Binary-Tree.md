# Balanced Binary Tree

题目来源：[Balanced Binary Tree ](https://oj.leetcode.com/problems/balanced-binary-tree/)

>
	
	Given a binary tree, determine if it is height-balanced.

	For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

解题思路：
	
递归. 

```cpp
	
	int depth(TreeNode * root){
        if(root == NULL) return 0;
        return std::max(depth(root->left),depth(root->right))+1;
    }
    bool isBalanced(TreeNode *root) 
    {
        if(root == NULL) return true;
        int left = depth(root->left);
        int right = depth(root->right);
        if (abs(left - right) > 1) return false;
        return isBalanced(root->left) && isBalanced(root->right);
    }

```

其实递归过程中好多都算重复了。 可以将判断过程融合在算高度的方法里。

```cpp
	
	int depth(TreeNode * root){
        if(root == NULL) return 0;
        int left = depth(root->left);
        int right = depth(root->right);
        if(left == -1 || right == -1 || abs(left-right) > 1) 
            return -1;
        return std::max(left, right)+1;
    }
    bool isBalanced(TreeNode *root) 
    {
        if(root == NULL) return true;
        return depth(root) >= 0;
    }
```
	



