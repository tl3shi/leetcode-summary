# Partition List

题目来源：[Partition List ](https://oj.leetcode.com/problems/partition-list/)

>
	Given a linked list and a value x, partition it such that all nodes less than x come before nodes greater than or equal to x.
	You should preserve the original relative order of the nodes in each of the two partitions.
	For example,
	Given 1->4->3->2->5->2 and x = 3,
	return 1->2->2->4->3->5.

解题思路：

注意一些边界情况， 要保持以前的两个节点顺序。不然就可以把小于x的一个一个往最前面插入。

```cpp
	
	ListNode *partition(ListNode *head, int x) 
    {
        ListNode dummy1(-1), dummy2(-1);
        ListNode * left = &dummy1;
        ListNode * right = &dummy2;
        ListNode * node = head;
        while(node)
        {
            if(node->val < x)
            {
                left->next = node;
                left = left->next;
            }else
            {
                right->next = node;
                right = right->next;
            }
            node = node->next;
        }
        left->next = dummy2.next;
        right->next = NULL;
        return dummy1.next;
    }
```
 

