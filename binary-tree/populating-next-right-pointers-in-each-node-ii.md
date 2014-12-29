# populating next right pointers in each node ii

题目来源：[Populating Next Right Pointers in Each Node II](https://oj.leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/)

>
	
	Follow up for problem "Populating Next Right Pointers in Each Node".
	What if the given tree could be any binary tree? Would your previous solution still work?
	
	Note:
	You may only use constant extra space.
	For example,
	Given the following binary tree,
	         1
	       /  \
	      2    3
	     / \    \
	    4   5    7
	After calling your function, the tree should look like:
	         1 -> NULL
	       /  \
	      2 -> 3 -> NULL
	     / \    \
	    4-> 5 -> 7 -> NULL
	    
解题思路：

跟 [Populating Next Right Pointers in Each Node](./populating-next-right-pointers-in-each-node.html)思路一致，值得注意的是

* 在填充下一层next时，当前层的next要找完。//Attention 0
* 往下走时，可能前面的节点没有孩纸节点，也要找完同一层的节点是否存在孩纸节点。//Attention 1

```cpp
void connect(TreeLinkNode *root) 
{
   while(root)
   {
       auto down = root->left;
       if(NULL == down) down = root->right;
       if(NULL == down) down = root->next;////Attention 1: no child of root, but maybe the next(or next') node has children, although the same level
       while(root)//go right
       {
           auto next = root->next; //go right to find next's children
           if(root->left)
           {
               if(root->right)
                   root->left->next = root->right;
               else{
                   while (next && (next->left == NULL && next->right == NULL)) //Attention 0
                       next = next->next;
                   if(next != NULL)
                       root->left->next = next->left == NULL ? next->right : next->left;
               }
           }
           if(root->right)
           {
               while (next && (next->left == NULL && next->right == NULL))
                   next = next->next;
               if(next != NULL)
                   root->right->next = next->left == NULL ? next->right : next->left;
           }
           root = next;
       }
       root = down;//go down
   }    
}
```

上面代码确实比较丑陋～  其实着眼于同一层之前通过pre来记录同一层的前一个节点的话，代码就好看得多。 [leetcode-cpp](https://github.com/soulmachine/leetcode)

```cpp
void connect(TreeLinkNode *root)
{
    while(root)
    {
        TreeLinkNode * next = NULL;//next level
        TreeLinkNode * pre = NULL;
        while(root)//go right
        {
            if(next == NULL) next = root->left ? root->left : root->right;
            if(root->left)
            {
                if(pre) pre->next = root->left;
                pre = root->left;
            }
            if(root->right)
            {
                if(pre) pre->next = root->right;
                pre = root->right;
            }
            root = root->next;
        }
        root = next;//goto next level
    }
}
```

