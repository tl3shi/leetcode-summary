# Reverse Nodes in k Group

题目来源：[Reverse Nodes in k-Group](https://oj.leetcode.com/problems/reverse-nodes-in-k-group/)

>
	Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.
	If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.
	You may not alter the values in the nodes, only nodes itself may be changed.
	Only constant memory is allowed.
	For example,
	Given this linked list: 1->2->3->4->5
	For k = 2, you should return: 2->1->4->3->5
	For k = 3, you should return: 3->2->1->4->5

解题思路：

每遇到k个，就reverse一下。值得注意的是：

- 输入list长度是否大于k个;
- 最后不足的k个;
- reverse 中间的一段前之前得backup一下当前段(tail)的下一个, 以防止reverse内部改变了tail->next值.

```cpp
//reverse [start, tail], return newhead
ListNode* reverse(ListNode* head, ListNode* tail)
{
    ListNode * pre = NULL;
    while(head != tail)
    {
        auto next = head->next;
        head->next = pre;
        pre = head;
        head = next;
    }
    head->next = pre; //do not forget tail
    return tail;
}
ListNode *reverseKGroup(ListNode *head, int k) 
{
    if(k <= 1 || head == NULL) return head;    
    ListNode * lastStart = NULL;
    ListNode * result = NULL;
    while(head)
    {
        int i = 1; 
        auto start = head;
        while(i++ < k && head != NULL)
            head = head->next;
        if(head != NULL)
        {
            auto end = head;
            auto nextbak = head->next;
            auto segStart = reverse(start, end);
            if (lastStart == NULL)  
                result = segStart;
            else 
                lastStart->next = segStart;
            lastStart = start;
            head = nextbak;
        }else//last segment
        {
            if(lastStart)
                lastStart->next = start;
            else //node len less than k
                return start;
        }
    }
    return result;
}
```
