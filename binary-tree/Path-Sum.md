# Path Sum

题目来源：[Path Sum](https://oj.leetcode.com/problems/path-sum/)

>
	Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
	For example:
	Given the below binary tree and sum = 22,
	              5
	             / \
	            4   8
	           /   / \
	          11  13  4
	         /  \      \
	        7    2      1
	return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

解题思路：

递归最简单了。

```cpp
bool solveRecusive(TreeNode *root, int sum) 
{
    int v = root->val;
    if(root->left == NULL && root->right == NULL)
        return v == sum;
    return (root->left && solveRecusive(root->left, sum-v)) ||
           (root->right && solveRecusive(root->right, sum-v));
}
bool hasPathSum(TreeNode *root, int sum) 
{
    if(root == NULL) return false;//test case rule
    return solveRecusive(root, sum);
}
```


