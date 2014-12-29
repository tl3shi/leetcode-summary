# Rotate List

题目来源：[Rotate List](https://oj.leetcode.com/problems/rotate-list/)

>
    Given a list, rotate the list to the right by k places, where k is non-negative.
    For example:
    Given 1->2->3->4->5->NULL and k = 2,
    return 4->5->1->2->3->NULL.

解题思路：

找出分隔点，注意对输入k值的处理，k可能超过链表长度。另外别忘了链表结尾要手动置为NULL。

```cpp
    
    int length(ListNode* head)
    {
        int len = 0;
        while(head)
            ++len, head = head->next;
        return len;
    }
    ListNode *rotateRight(ListNode *head, int k) 
    {
        if(head == NULL || head->next == NULL || k == 0) return head;
        int len = length(head);
        k = k % len;
        if(k == 0) return head;
        ListNode * newHead = NULL;
        ListNode * headbak = head;
        int i = 1;
        while(i < len-k)
            head = head->next, i++;
        newHead = head->next;
        head->next = NULL; //!!! important
        ListNode *tail = newHead;
        while(tail->next)
            tail = tail->next;
        tail->next = headbak;
        return newHead;
    } 
```


