# Sum Root to Leaf Numbers

题目来源：[Sum Root to Leaf Numbers](https://oj.leetcode.com/problems/sum-root-to-leaf-numbers/)

>
    
    Given a binary tree containing digits from 0-9 only, each root-to-leaf path
    could represent a number.
    An example is the root-to-leaf path 1->2->3 which represents the number
    123.
    Find the total sum of all root-to-leaf numbers.
    For example,
       1
      / \
     2   3
     The root-to-leaf path 1->2 represents the number 12.
     The root-to-leaf path 1->3 represents the number 13.
     Return the sum = 12 + 13 = 25.

解题思路：

直接dfs，将到达叶节点代表的数字加起来即可。

```cpp

	void dfs(long long input, TreeNode* node, long long &result)
    {
        assert(node != NULL);
        long long cur = input * 10 + node->val;
        if(node->left == NULL && node->right == NULL) //leaf
        {
            result += cur;
            return;
        }
        if(node->left)
            dfs(cur, node->left, result);
        if(node->right)
            dfs(cur, node->right, result);
    }
    int sumNumbers(TreeNode *root) 
    {
        if(root == NULL) return 0;   
        long long result = 0L;
        dfs(0, root, result);
        return (int)result;
    }
```

