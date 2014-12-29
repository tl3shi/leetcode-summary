# Binary Tree Postorder Traversal

题目来源： [Binary Tree Postorder Traversal](https://oj.leetcode.com/problems/binary-tree-postorder-traversal/)

>
	Given a binary tree, return the postorder traversal of its nodes' values.
	For example:
	Given binary tree {1,#,2,3},
	   1
	    \
	     2
	    /
	   3
	return [3,2,1].
	Note: Recursive solution is trivial, could you do it iteratively?
 


解题思路：

下文用了5种方法实现了对二叉树进行后序遍历。

### 思路一: 直接递归

```cpp
	
	void postRecursion(TreeNode * root, vector<int> &path)
	{
	    if(root == NULL) return;
	    if(root->left != NULL)
	        postRecursion(root->left, path);
	    if(root->right != NULL)
	        postRecursion(root->right, path);
	    path.push_back(root->val);
	}

	vector<int> postorderTraversal(TreeNode *root) 
	{
	    vector<int> result;
	    postRecursion(root, result);
	    return move(result);
	}
```

### 思路二: 非递归. 仿造先序,因为先序的非递归很好写.

(来自寝室哥们ZZ大神的思路)
	
	先序: `中左右` 
	后序: `左右中` 

发现 先序.reverse = `右左中` 将`右左`交换就得到`左右中`.
即将原来的先序变通下就有了下面的算法.

```cpp

    vector<int> postFakePre(TreeNode * root)
    {
        stack<TreeNode*> stacks;
        stacks.push(root);
        vector<int> result;
        while(! stacks.empty())
        {
            auto node = stacks.top();
            result.push_back(node->val); stacks.pop();
            //pre: push right then left, 
            //fake pre: push left, then right
            if(node->left != NULL)
                stacks.push(node->left);
            if(node->right != NULL)
                stacks.push(node->right);
        }
        std::reverse(result.begin(), result.end());
        return move(result);
    }
```

### 思路三：传统方法

用一个指针last记录上一次访问的节点来区分右孩纸是否已经访问过了该回归到父节点。代码如下

```cpp

	vector<int> postNormal(TreeNode * root)
    {
        stack<TreeNode*> stacks;
        vector<int> result;
        TreeNode* last = NULL, * cur = root;
        while(true)
        {
            if(cur != NULL)//go to left most
            {
                stacks.push(cur);
                cur = cur->left;
            }else //leaf node
            {
                auto peak = stacks.top();
                if(peak->right != NULL && peak->right != last) // right child has not been visited
                {
                    cur = peak->right;
                }else{
                    result.push_back(peak->val);
                    stacks.pop();
                    last = peak;
                    if(stacks.empty()) 
                        break;
                }
            }
        }
        return move(result);
    }
```

### 思路四：改进的传统方法

下面的方法来自网络(但忘了具体出处了). 比较好理解。

>
	要保证根结点在左孩子和右孩子访问之后才能访问，因此对于任一结点P，先将其入栈。
		如果P不存在左孩子和右孩子，则可以直接访问它；或者P存在左孩子或者右孩子，但是其左孩子和右孩子都已被访问过了，则同样可以直接访问该结点。
		若非上述两种情况，则将P的右孩子和左孩子依次入栈，这样就保证了每次取栈顶元素的时候，左孩子在右孩子前面被访问，左孩子和右孩子都在根结点前面被访问。

代码如下:

```cpp

	vector<int> postNormalBetter(TreeNode * root)
    {
        stack<TreeNode*> stacks;
        vector<int> result;
        TreeNode* last = NULL;
        stacks.push(root);
        while(! stacks.empty())
        {
            auto cur = stacks.top();
            if ( (NULL == cur->left && NULL == cur->right) //is leaf node or
                || (last && (last == cur->left || last == cur->right)) )// children have been visited
                {
                    result.push_back(cur->val);
                    stacks.pop();
                    last = cur;
                }
            else//has children, push right then left
            { 
                if(cur->right)
                    stacks.push(cur->right); 
                if(cur->left)
                    stacks.push(cur->left);
            }
        }
        return move(result);
    }
```

### 思路五：Morris遍历

以上都用了`O(n)`的时间+`O(n)`的空间.
还有就是传说中的利用了线索二叉树`O(1)`的空间的`Morris遍历算法`.
主要就是利用了叶子节点的孩纸指针, 指向后继节点记录回退的位置。
[这篇文章](http://www.cnblogs.com/AnnieKim/archive/2013/06/15/MorrisTraversal.html)讲得清晰，我就不重复了。
将后续遍历的算法copy过来.

>
	后序遍历稍显复杂，需要建立一个临时节点dump，令其左孩子是root。并且还需要一个子过程，就是倒序输出某两个节点之间路径上的各个节点。
    步骤：
    当前节点设置为临时节点dump。
    1. 如果当前节点的左孩子为空，则将其右孩子作为当前节点。
    2. 如果当前节点的左孩子不为空，在当前节点的左子树中找到当前节点在中序遍历下的前驱节点。
       a) 如果前驱节点的右孩子为空，将它的右孩子设置为当前节点。当前节点更新为当前节点的左孩子。
       b) 如果前驱节点的右孩子为当前节点，将它的右孩子重新设为空。倒序输出从当前节点的左孩子到该前驱节点这条路径上的所有节点。当前节点更新为当前节点的右孩子。
    3. 重复以上1、2直到当前节点为空。


```cpp

	vector<int> reverse(TreeNode * from, TreeNode * to)
	{
	    vector<int> path;
	    while(true)
		{
	        path.push_back(from->val);
	        if(from == to)
	            break;
	        from = from->right;
	    }
	    std::reverse(path.begin(), path.end());
    return move(path);
	}
	vector<int> postMorris(TreeNode * root)
	{
	    TreeNode dump(-1);
	    dump.left = root;
	    TreeNode * cur = &dump;
	    vector<int> result;
	    while(cur != NULL)
	    {
	        if(NULL == cur->left) //1
	            cur = cur->right;
	        else//2
	        {
	            auto pre = cur->left; //pre: left child's right most
	            while(pre->right != NULL && pre->right != cur)
	                pre = pre->right;
	            if(pre->right == NULL)//2.a
	            {
	                pre->right = cur;
	                cur = cur->left;
	            }else // 2.b
	            {
	                pre->right = NULL;
	                auto path = reverse(cur->left, pre);
	                std::copy(path.begin(), path.end(), back_insert(result));
	                cur = cur->right;
	            }
	        }
	    }
	    return move(result);
	}
```

