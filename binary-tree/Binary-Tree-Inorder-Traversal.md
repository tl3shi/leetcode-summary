# Binary Tree Inorder Traversal

题目来源： [Binary Tree Inorder Traversal](https://oj.leetcode.com/problems/binary-tree-Inorder-traversal/)

>
	Given a binary tree, return the inorder traversal of its nodes' values.
	For example:
	Given binary tree {1,#,2,3},
	   1
	    \
	     2
	    /
	   3
	return [1,3,2].
	Note: Recursive solution is trivial, could you do it iteratively?

解题思路：


###  思路一: 直接递归(略)

###  思路二: 用stack.

```cpp
vector<int> inorderNormal(TreeNode * root)
{
    vector<int> result;
    stack<TreeNode*> stacks;
    TreeNode * cur = root;
    while(true)
    {
        if(cur != NULL)
        {
            stacks.push(cur);
            cur = cur->left;
        }else
        {
            if(stacks.empty()) break;
            cur = stacks.top(); stacks.pop();
            result.push_back(cur->val);
            if(stacks.empty())
                break;
            cur = cur->right;
	
        }
    }
    return move(result);
}
vector<int> inorderTraversal(TreeNode *root)
{
    if(root == NULL) return vector<int>();
    return inorderNormal(root);
}
```

###  思路三： Morris遍历. `O(1)`空间 + `O(n)`时间

利用线索二叉树, 利用叶子节点的空指针指向前驱后继来记住状态。算法仍参考[Morris Traversal](http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html)，里面讲了详细的案例。


具体算法如下:
    
	步骤：
	1. 如果当前节点的左孩子为空，则输出当前节点并将其右孩子作为当前节点。
	2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
	   a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
	   b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空（恢复树的形状）。输出当前节点。当前节点更新为当前节点的右孩子。
	3. 重复以上1、2直到当前节点为空。

```cpp
vector<int> inorderMorris(TreeNode * root)
{
    vector<int> result;
    TreeNode * cur = root;
    while(NULL != cur)
    {
        if(cur->left == NULL)
        {
            result.push_back(cur->val);
            cur = cur->right;
        }else
        {
            auto pre = cur->left;
            while(pre->right != NULL && pre->right != cur)
                pre = pre->right;
            if(pre->right == NULL)
            {
                pre->right = cur;
                cur = cur->left;
            }else //reset
            {
                pre->right = NULL;
                result.push_back(cur->val);
                cur = cur->right;
            }
        }
    }
    return move(result);
}
```

