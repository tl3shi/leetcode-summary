# Remove Nth Node From End of List

题目来源：[Remove Nth Node From End of List](https://oj.leetcode.com/problems/remove-nth-node-from-end-of-list/)

>
	Given a linked list, remove the nth node from the end of list and return its head.
	For example,
	   Given linked list: 1->2->3->4->5, and n = 2.
	   After removing the second node from the end, the linked list becomes 1->2->3->5.
	Note:
	Given n will always be valid.
	Try to do this in one pass.

解题思路：

快慢指针的思路, 先走n步，然后另外一个节点从头开始，直到先走的那个节点到达结尾，第二次从头开始的那个点极为要删除的那个节点。 注意边界条件可能要删除头。

```cpp
ListNode *removeNthFromEnd(ListNode *head, int n) 
{
    assert(head != NULL);
    //n is valid
    int k = 0;
    ListNode *headbak = head;
    while(k++ < n)
        head = head->next;
    ListNode * pre = headbak;
    if(head == NULL) //delete head
    {
        ListNode * result = headbak->next;
        delete pre;
        return result;
    }
    while(head->next)
    {
        pre = pre->next;
        head = head->next;
    }
    //delete pre->next;
    auto deleted = pre->next;
    auto next = deleted->next;
    pre->next = next;
    delete deleted;
    return headbak;
}
```
