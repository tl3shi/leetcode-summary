# Remove Duplicates from Sorted List

题目来源：[Remove Duplicates from Sorted List](https://oj.leetcode.com/problems/remove-duplicates-from-sorted-list/)

>
	Given a sorted linked list, delete all duplicates such that each element appear only once.
	For example,
	Given 1->1->2, return 1->2.
	Given 1->1->2->3->3, return 1->2->3.

解题思路：
	
```cpp
	
	ListNode *deleteDuplicates(ListNode *head) 
    {
        ListNode * result = head;
        ListNode * resultBak = result;
        while(head)
        {
            while(head != NULL && head->val == result->val)
                //free 'head'
                head = head->next;
            result->next = head;///result->val != head
            result = result->next;
        }    
        return resultBak;
    }
```

把与上一个节点相同的值略过， [1] {1 1} 2 2 ... 
上面代码保留相同中的第一个， 会造成内存泄漏。 
下面代码是保留相同中的最后一个，之前的都delete掉。

```cpp 

	ListNode *deleteDuplicates(ListNode *head) 
    {
        if(head == NULL || head->next == NULL) return head;
        ListNode dummy(-1);
        ListNode * result = &dummy;
        while(head)
        {
            while(head != NULL && head->next != NULL && head->val == head->next->val)
            {
                auto next = head->next;  //1 1 1 2
                delete head;//free 'head'
                head = next;
            }
            result->next = head;
            result = result->next;
            if(head) head = head->next;
        }    
        return dummy.next;
    }
```


