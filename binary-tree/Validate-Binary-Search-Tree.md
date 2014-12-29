# Validate Binary Search Tree

题目来源：[Validate Binary Search Tree](https://oj.leetcode.com/problems/validate-binary-search-tree/)

>
	Given a binary tree, determine if it is a valid binary search tree (BST).
	Assume a BST is defined as follows:	
	The left subtree of a node contains only nodes with keys less than the node's key.
	The right subtree of a node contains only nodes with keys greater than the node's key.
	Both the left and right subtrees must also be binary search trees.

解题思路：

###  递归判断节点值是否满足条件

```cpp
	
	bool _isBST(TreeNode * node, int min_, int max_)
    {
        if(node == NULL) return true;
        if(node->val <= min_ || node->val >= max_) return false;
        return _isBST(node->left, min_, node->val)
             && _isBST(node->right, node->val, max_);
    }
    bool isValidBST(TreeNode *root) 
    {
        return _isBST(root, INT_MIN, INT_MAX);
    }
```

###  中序遍历

BST 中序遍历结果是升序。 中序遍历的方法就多了，有递归、迭代、Morris遍历等，详情可以参考[binary-tree-inorder-traversal](./binary-tree-inorder-traversal.html), 下面就只列一种了。

```cpp
	
	bool isValidBST(TreeNode *root) 
    {
        stack<TreeNode*> stacks;
        TreeNode * node = root;
        int last = INT_MIN;
        while(true)
        {
            if(node)
            {
                stacks.push(node);
                node = node->left;
            }else
            {
                if(stacks.empty()) break;
                node = stacks.top(); stacks.pop();
                if(last >= node->val) return false;
                last = node->val;
                node = node->right;
            }
        }
        return true;
    }
```

再训练下Morris遍历。
跟[recover-binary-search-tree](./recover-binary-search-tree.html)一样，还是得强调下，Morris遍历中找到不是升序了，也不能return。因为修改了原来树的结构，必须rollback完毕才OK。

```cpp
	
	bool isValidBST(TreeNode *root) 
    {
        TreeNode * node = root;
        int last = INT_MIN;
        bool result = true;
        while(node)
        {
            if(node->left == NULL)
            {
                if(last >= node->val) result = false;;
                last = node->val;
                node = node->right;
            }else
            {
                auto pre = node->left;
                while(pre->right != NULL && pre->right != node)
                    pre = pre->right;
                if(pre->right == NULL)
                {
                    pre->right = node;
                    node= node->left;
                }else
                {
                    if(last >= node->val) result = false;//cannot return. return false;
                    pre->right = NULL;//reset
                    last = node->val;
                    node = node->right;   
                }
            }
        }
        return result;
    }
```


