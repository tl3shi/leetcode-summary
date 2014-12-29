# Construct Binary Tree from Inorder and Postorder Traversal

题目来源：[Construct Binary Tree from Inorder and Postorder Traversal](https://oj.leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/)

>
	Given inorder and postorder traversal of a tree, construct the binary tree.
	Note:
	You may assume that duplicates do not exist in the tree.


解题思路：

仍跟上题一样[construct-binary-tree-from-preorder-and-inorder-traversal](./construct-binary-tree-from-preorder-and-inorder-traversal.html),同样假设输入合理。
若输入不合法，可参考[树重建](http://tanglei.me/data%20structure/dsa-rebuild-tree.html)进行处理。
	
	中：左  中  右
	后：左  右  中
	在中序中查找后序的最后一个得index为left
	left_len = left - in_start
	对左子树而言: 
	中序左: [in_start, left - 1]
	后序左: [post_start, post_start + left_len -1]
	同理 右子树
	中序右: [left+1, in_end]
	后序右: [post_start + left_len, post_end-1]
	
```cpp
	
	TreeNode * buildRecursion(vector<int> &postorder, vector<int> &inorder,
                        int postStart, int postEnd, int inStart, int inEnd)
        {
            if(postStart > postEnd) return NULL;
            if(postEnd == postStart) 
                return new TreeNode(postorder[postStart]);
            TreeNode * root = new TreeNode(postorder[postEnd]);
            int index = inStart;
            while(inorder[index] != root->val) //assuming can get, or else should check if index > inEnd
                index++;
            int leftLen = index - inStart;
            int rightLen = inEnd - index;
            root->left = buildRecursion(postorder, inorder, postStart, postStart+leftLen-1, inStart, index-1);
            root->right = buildRecursion(postorder, inorder, postStart+leftLen, postEnd-1, index+1, inEnd);
            return root;
        }
    TreeNode *buildTree(vector<int> &inorder, vector<int> &postorder) 
    {
        return    buildRecursion(postorder, inorder, 0, postorder.size()-1, 0, inorder.size()-1); 
    }
```


