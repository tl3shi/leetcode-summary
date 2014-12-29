# Unique Binary Search Trees II

题目来源：[Unique Binary Search Trees II](https://oj.leetcode.com/problems/unique-binary-search-trees-ii/)

>
    Given n, generate all structurally unique BST's (binary search trees) that
    store values 1...n.
    For example,
    Given n = 3, your program should return all 5 unique BST's shown below.

      1         3     3      2      1
       \       /     /      / \      \
        3     2     1      1   3      2
        /     /       \                 \
       2     1         2                 3

解题思路：

跟上题[Unique Binary Search Trees](./unique-binary-search-trees-ii.html)一样，这个题目需要返回具体的结果。

```cpp
vector<TreeNode*> generateTreesRec(int start, int end)
{
    vector<TreeNode *> result;
    if(start >= end)
    {
        if(start > end)
           result.push_back(NULL);
       else
           result.push_back(new TreeNode(start));
       return move(result);
    }
    for(int i = start; i <= end; i++)
    {
        auto left = generateTreesRec(start, i-1);
        auto right = generateTreesRec(i+1, end);
        for(auto it1 = left.begin(); it1 != left.end(); it1++)
           for(auto it2 = right.begin(); it2 != right.end(); it2++)
           {
               TreeNode* root = new TreeNode(i);
               root->left = *it1;
               root->right = *it2;
               result.push_back(root);
           }
    }
    return move(result);
}

vector<TreeNode *> generateTrees(int n)
{
   return generateTreesRec(1, n);//n==0, return TreeNode is NULL, included.
}
```

注意当end>start的时候也要返回一个空的Node，因为后面的遍历时，直接用left/right都有的情况才生成新的node。

