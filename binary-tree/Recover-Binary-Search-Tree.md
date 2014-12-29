# Recover Binary Search Tree

题目来源：[Recover Binary Search Tree](https://oj.leetcode.com/problems/recover-binary-search-tree/)

>
	Two elements of a binary search tree (BST) are swapped by mistake.	Recover the tree without changing its structure.	Note:	A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?

解题思路：

###  求得中序遍历结果,再两边向中间扫描

O(2*n) 空间解法～
直接中序遍历，然后分别从前往后、从后往前找非升序、非降序的两个node，交换其值即可。

```cpp
	
	void inorder1(vector<TreeNode*> &result, TreeNode* root)
	{
	    if(root->left) inorder1(result, root->left);
	    result.push_back(root);
	    if(root->right) inorder1(result, root->right);
	}
	
	void recoverTree1(TreeNode *root)
	{
	    if (root == NULL) return;
	    vector<TreeNode*> inorder_result;
	    inorder1(inorder_result, root);
	    TreeNode* firstWrong = NULL, *secondWrong = NULL;
	    vector<TreeNode*>::iterator it;
	    for(it = inorder_result.begin(); it != inorder_result.end()-1; it++)
	    {
	        if((*it)->val >= (*(it+1))->val)
	        {
	            firstWrong = *it;
	            break;
	        }
	    }
	    for(auto it2 = inorder_result.end()-1; it2 != it; it2--)
	    {
	        if((*it2)->val <= (*(it2-1))->val)
	        {
	            secondWrong = *it2;
	            break;
	        }
	    }
	    //swap
	    int tmp = firstWrong->val;
	    firstWrong->val = secondWrong->val;
	    secondWrong->val = tmp;
	}
```

###  中序遍历一边遍历，一边扫描。

当两个节点都找到后，即可退出中序遍历流程。

```cpp
	
	void recoverTree(TreeNode *root) 
    {
        if(root == NULL) return;
        stack<TreeNode*> stacks;
        TreeNode tmp(INT_MIN);
        TreeNode * last = &tmp;
        TreeNode * node1 = NULL, *node2 = NULL;
        TreeNode * node = root;
        while(true)
        {
            if(node)
            {
                stacks.push(node); 
                node = node->left;
            }
            else
            {
                if(stacks.empty()) break;
                node = stacks.top(); stacks.pop();
                if(last->val >= node->val)
                {
                    if(node1 == NULL)
                        {node1 = last; node2=node;}//3,2
                    else
                        node2 = node;
                }
                last = node;
                node = node->right;
            }
        }
        std::swap(node1->val, node2->val);
    }
```

###  Morris遍历，常数空间。

算法解释见[binary-tree-inorder-traversal](./binary-tree-inorder-traversal.html);

注意*找出两个node后还得让遍历走完～以避免之前的改动revert完毕*，否则可能会造成oj check时死循环(传入的树结构修改后不对).

```cpp
	
	void recoverTree(TreeNode *root) 
    {
        if(root == NULL) return;
        TreeNode* node1 = NULL, *node2 = NULL;
        TreeNode * pre = NULL;
        TreeNode * node = root;
        TreeNode  tmp(INT_MIN); 
        TreeNode * last = &tmp;
        while(node)
        {
            if(node->left == NULL)
            {
                //visit node
                if(last->val >= node->val){
                    if(node1 == NULL)
                        {node1 = last; node2 = node;}
                    else
                        node2 = node;//can not break;
                } 
                last = node;
                node = node->right;
            }
            else
            {
                pre = node->left;
                while(pre->right != NULL && pre->right != node)
                    pre = pre->right;
                if(pre->right == NULL)
                {
                    pre->right = node;
                    node = node->left;
                }
                else
                {
                    pre->right = NULL;
                    //visit node
                    if(last->val >= node->val){
                        if(node1 == NULL)
                            {node1 = last; node2 = node;}
                        else
                            node2 = node;//can not break;
                    }
                    last = node;
                    node = node->right;
                }
            }
        }
        std::swap(node1->val, node2->val);
    }
```


