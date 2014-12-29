# Linked List Cycle

题目来源：[Linked List Cycle](https://oj.leetcode.com/problems/linked-list-cycle/)

>

    Given a linked list, determine if it has a cycle in it.

解题思路：

简单的快慢指针.

```cpp

    bool hasCycle(ListNode *head) 
    {
        if(head == NULL || head->next == NULL) return false;
        ListNode * fast = head;
        ListNode * slow = head;
        while(fast != NULL && fast->next != NULL){
            fast = fast->next->next;
            slow = slow->next;
            if(fast == slow) return true;
        }
        return false;
    }
```

