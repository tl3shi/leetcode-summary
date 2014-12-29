# Populating Next Right Pointers in Each Node

题目来源：[Populating Next Right Pointers in Each Node](https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node/)

>

	Given a binary tree

    struct TreeLinkNode {
      TreeLinkNode *left;
      TreeLinkNode *right;
      TreeLinkNode *next;
    }
	Populate each next pointer to point to its next right node. If there is no next right node, the next pointer should be set to NULL.
	
	Initially, all next pointers are set to NULL.
	
	Note:
	
	You may only use constant extra space.
	You may assume that it is a perfect binary tree (ie, all leaves are at the same level, and every parent has two children).
	For example,
	Given the following perfect binary tree,
	         1
	       /  \
	      2    3
	     / \  / \
	    4  5  6  7
	After calling your function, the tree should look like:
	         1 -> NULL
	       /  \
	      2 -> 3 -> NULL
	     / \  / \
	    4->5->6->7 -> NULL
解题思路：

1种方法是领取数组把每一层存起来，然后连接。不过非常数空间。
另外就是常数空间解法。

```cpp
	
void connect(TreeLinkNode *root) 
{
   while(root)
   {
       auto left = root->left;
       while(root) //go right
       {
           if(root->left && root->right)
               root->left->next = root->right;
           if(root->right && root->next)
               root->right->next = root->next->left;
           root = root->next;
       }
       root = left;//go down
   }
}
```
还有的写法就是 [Populating Next Right Pointers in Each Node II](./populating-next-right-pointers-in-each-node-ii.html)了，完全可以用于解这个题目。


 

