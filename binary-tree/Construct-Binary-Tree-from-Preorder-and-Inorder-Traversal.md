# Construct Binary Tree from Preorder and Inorder Traversal

题目来源：[Construct Binary Tree from Preorder and Inorder Traversal](https://oj.leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/)

>

    Given preorder and inorder traversal of a tree, construct the binary tree.
    Note:
    You may assume that duplicates do not exist in the tree.

解题思路：

递归比较好～但注意下标别搞错.
这里假设输入一定可以构造合理的二叉树。所以没有考虑一些异常情况。这里[树重建](http://tanglei.me/data%20structure/dsa-rebuild-tree.html)有考虑不能成功构造出二叉树的情况。

	先序：中     左     右
	中序：左     中     右
	先序左：[pre_start+1, pre_start + 1 + left_len - 1]
	中序左：[in_start, left-1]
	
	先序右：[pre_start+left_len+1, pre_end]
	中序右：[left+1, in_end]

```cpp
	
	//assuming always can get right result
    TreeNode * buildRecursion(vector<int> &preorder, vector<int> &inorder,
                            int preStart, int preEnd, int inStart, int inEnd)
    {
        if(preStart > preEnd) return NULL;
        if(preEnd == preStart) // assert(inStart == inEnd)
            return new TreeNode(preorder[preStart]);
        TreeNode * root = new TreeNode(preorder[preStart]);
        int index = inStart;
        while(inorder[index] != root->val) //assuming can get, or else should check if index > inEnd 
            index++;
        int leftLen = index - inStart;
        int rightLen = inEnd - index;
        root->left = buildRecursion(preorder, inorder, preStart+1, preStart+leftLen, inStart, index-1);
        root->right = buildRecursion(preorder, inorder, preStart+leftLen+1, preEnd, index+1, inEnd);
        return root;
    }
    TreeNode *buildTree(vector<int> &preorder, vector<int> &inorder) 
    {
        return buildRecursion(preorder, inorder, 0, preorder.size()-1, 0, inorder.size()-1);
    }
```

