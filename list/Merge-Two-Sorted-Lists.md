# Merge Two Sorted Lists

题目来源：[Merge Two Sorted Lists](https://oj.leetcode.com/problems/merge-two-sorted-lists/)

>
	Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

解题思路：

用一个多余的节点在头部，使得代码简洁，不然得去内部判断到底哪个节点当作新list的head。

```cpp
	
	ListNode *mergeTwoLists(ListNode *l1, ListNode *l2) 
    {
        ListNode dummy(-1);
        ListNode * pre = &dummy;
        while(l1 && l2)
        {
            if (l1->val <= l2->val)
                pre->next = l1, l1 = l1->next;
            else 
                pre->next = l2, l2 = l2->next;
            pre = pre->next;
        }
        if (l1 != NULL)
            pre->next = l1;
        else
            pre->next = l2;
        return dummy.next;
    }
```

 

