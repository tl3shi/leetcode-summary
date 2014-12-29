# Convert Sorted List to Binary Search Tree

题目来源：[Convert Sorted List to Binary Search Tree](https://oj.leetcode.com/problems/convert-sorted-list-to-binary-search-tree/)

>
	Given a singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

解题思路：

###  tricky 方法, 另外取O(n)空间

偷懒方法，另外取另外取O(n)空间把list的数据取出来放入数组，然后跟[](./convert-sorted-array-to-binary-search-tree.html)题目一样用数组的方式去做。
代码就略过了。
虽然不是出题者的本意～ 但...... 你咬我呀.

###  O(nlogn)时间

每次用O(len/2)的时间去把中间的节点找出来。然后跟数组一样的方式解决。时间复杂度为O(nlogn).中途找mid不跟数组一样O(1).

```cpp
	
	int length(ListNode * head)
    {
        int len = 0;
        while(head)
        {
            ++len; 
            head = head->next;
        }
        return len;
    }
    TreeNode * convert(ListNode * head, int len)
    {
        if(head == NULL || len == 0) return NULL;
        if(len == 1) return new TreeNode(head->val);
        int mid = len>>1;
        ListNode * pre = head;
        int i = mid;
        while(--i)
            pre=pre->next;
        int leftlen = mid-1; int rightlen = len-mid;//even
        if(len & 0x1)
        {
            pre = pre->next;
            leftlen = mid;
            rightlen = len-mid-1;
        }   
        auto root = new TreeNode(pre->val);
        root->left = convert(head, leftlen);
        root->right = convert(pre->next, rightlen);
    }
    
    TreeNode *sortedListToBST(ListNode *head) 
    {
        int len = length(head);
        return convert(head, len);
    }
```

从底至上构造Tree, 递归(得忽略递归调用的时间/空间消耗)调用，递归中传同一个链表，链表不停往前走，通过下标关系来控制左右子树。进入递归时链表指向头节点，结束递归时，链表指向尾节点的next。

下面代码中，每次递归调用开始时，节点指针都指向区间第一个，结束时节点的指针指向*区间末尾的后一个*。每次递归调用时，分成左右两部分，左边构造完时，正好指针指向mid，创建一下root，继续构造右部分子树。[ref](http://www.cnblogs.com/lautsie/p/3346581.html)

```cpp
	
	int length(ListNode * head)
    {
        int len = 0;
        while(head)
        {
            ++len; 
            head = head->next;
        }
        return len;
    }
    TreeNode * convert(ListNode * &head, int start, int end)
    {
        assert(start <= end);
        if(start == end) {
            auto result = new TreeNode(head->val); 
            head=head->next;
            return result;
        }
        TreeNode* left = NULL;
        int mid = start + ((end-start)>>1);
        if(start <= mid-1)
            left = convert(head, start, mid-1);
        TreeNode * root = new TreeNode(head->val);
        head = head->next;
        root->left = left;
        if(mid+1 <= end)
            root->right = convert(head, mid+1, end);
        return root;
    }
    
    TreeNode *sortedListToBST(ListNode *head) 
    {
        if(head == NULL) return NULL;
        int len = length(head);
        return convert(head, 0, len-1);
    }
```

或许 convert这样写更简洁。

```cpp
	
	TreeNode * convert(ListNode * &head, int start, int end)
    {
        if(start > end) return NULL;
        int mid = start + ((end-start)>>1);
        TreeNode* left = convert(head, start, mid-1);
        TreeNode * root = new TreeNode(head->val);
        head = head->next;
        root->left = left;
        root->right = convert(head, mid+1, end);
        return root;
    }
```

