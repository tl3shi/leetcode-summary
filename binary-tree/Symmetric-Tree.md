# Symmetric Tree

题目来源：[Symmetric Tree](https://oj.leetcode.com/problems/symmetric-tree/)

>
	Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).	For example, this binary tree is symmetric:	    1	   / \	  2   2	 / \ / \	3  4 4  3	But the following is not:	    1	   / \	  2   2	   \   \	   3    3	Note:	Bonus points if you could solve it both recursively and iteratively.
	
解题思路：
左节点的左子树 ＝ 右节点的由子树。 
解题方法跟[same tree](./same-tree.html)差不多。

### 递归

```cpp
	
	bool isSymmetric(TreeNode* node1, TreeNode* node2)    {        if(node1 == NULL && node2 == NULL) return true;        if(node1 == NULL || node2 == NULL) return false;        if(node1->val != node2->val ) return false;        return isSymmetric(node1->left, node2->right) && isSymmetric(node1->right, node2->left);    }    bool isSymmetric(TreeNode *root)     {        if(root == NULL) return true;            return isSymmetric(root->left, root->right);    }
```

### 迭代

```cpp

	bool isSymmetric(TreeNode *root)    {        if(root == NULL) return true;        stack<TreeNode*> q;        q.push(root->left);        q.push(root->right);        while(! q.empty())        {            auto right = q.top(); q.pop();            auto left = q.top(); q.pop();            if(left == NULL && right == NULL) continue;            if(left == NULL || right == NULL) return false;            if(left->val != right->val) return false;            q.push(right->left);            q.push(left->right);            q.push(left->left);            q.push(right->right);        }        return true;    }
```
 


