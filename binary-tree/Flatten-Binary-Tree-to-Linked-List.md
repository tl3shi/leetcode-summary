# Flatten Binary Tree to Linked List

题目来源：[Flatten Binary Tree to Linked List ](https://oj.leetcode.com/problems/flatten-binary-tree-to-linked-list/)

>

	Given a binary tree, flatten it to a linked list in-place.
	For example,
	Given
	
	         1
	        / \
	       2   5
	      / \   \
	     3   4   6
	The flattened tree should look like:
	   1
	    \
	     2
	      \
	       3
	        \
	         4
	          \
	           5
	            \
	             6
	Hints: If you notice carefully in the flattened tree, each node's right child points to the next node of a pre-order traversal.

解题思路：

先序遍历，可以遍历完后再连接，也可以在遍历过程中连接。

```cpp
	
	void flatten(TreeNode *root) 
    {
        if(root == NULL) return;
        vector<TreeNode*> prefs;
        stack<TreeNode*> stacks;
        stacks.push(root);
        while(! stacks.empty())
        {
            auto node = stacks.top(); stacks.pop();
            prefs.push_back(node);
            if(node->right)
                stacks.push(node->right);
            if(node->left)
                stacks.push(node->left);
        }
        for(int i = 0; i < prefs.size()-1; i++)
        {
            prefs[i]->left = NULL;
            prefs[i]->right = prefs[i+1];
        }
    }
```

或者

```cpp
	
	void flatten(TreeNode *root) 
    {
        if(root == NULL) return;
        stack<TreeNode*> stacks;
        stacks.push(root);
        TreeNode tmp(-1);
        TreeNode* last = &tmp;
        while(! stacks.empty())
        {
            auto node = stacks.top(); stacks.pop();
            last->right = node;
            last->left = NULL;
            last = node;
            if(node->right)
                stacks.push(node->right);
            if(node->left)
                stacks.push(node->left);
        }
    }
```

或者用其他binary tree pre traverse 的方法都行。

