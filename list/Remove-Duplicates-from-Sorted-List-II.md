# Remove Duplicates from Sorted List II

题目来源：[Remove Duplicates from Sorted List II](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list-ii/)

>
	Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
	For example,
	Given 1->2->3->3->4->4->5, return 1->2->5.
	Given 1->1->1->2->3, return 2->3.

解题思路：

用一个变量标记是否有相同的节点，直到不同的才连接到result中。

```cpp
	
	ListNode *deleteDuplicates(ListNode *head) 
    {
        ListNode dummy(-1);
        ListNode * result = &dummy;
        while(head)
        {
            auto node = head->next; 
            bool rep = false;
            while(node != NULL && node->val == head->val)
            {
                auto next = node->next;
                delete node;
                node = next;
                rep = true;
            }
            if(rep) //1 1 1 2 2
                {delete head; head = node;}
            else //1 2 2
                {result->next = head; result = result->next;  head = head->next;}
        }
        result->next = NULL; //!!IMPORTANT
        return dummy.next;
    }
```
别忘了最后的节点->next需要置空。


