# Reverse Linked List II

题目来源：[Reverse Linked List II](https://oj.leetcode.com/problems/reverse-linked-list-ii/)

>
    Reverse a linked list from position m to n. Do it in-place and in one-pass.
    For example:
    Given 1->2->3->4->5->NULL, m = 2 and n = 4,
    return 1->4->3->2->5->NULL.
    Note:
    Given m, n satisfy the following condition:
    1 ≤ m ≤ n ≤ length of list.

解题思路：
画个图 较清晰。

	1-> 2->3 -> 4->5->NULL
	pre m cur next
	pre不变, 一个一个插入到pre后面.

```cpp
ListNode *reverseBetween(ListNode *head, int m, int n)
{
    if(m == n) return head;
    ListNode dummy(-1);
    ListNode * pre = &dummy;
    pre->next = head;
    int i = 1;
    while(i++ < m)
        pre = pre->next;
    
    //reverse between [m n]
    ListNode * mthNode = pre->next;
    ListNode * cur = mthNode->next, *next = NULL;
    while(m++ < n)
    {
        next = cur->next;
        cur->next = pre->next;
        pre->next = cur;
        cur=next;
    }
    mthNode->next = next;
    return dummy.next;
}	
```


