# Swap Nodes in Pairs

题目来源：[Swap Nodes in Pairs](https://oj.leetcode.com/problems/swap-nodes-in-pairs/)

>
	Given a linked list, swap every two adjacent nodes and return its head.
	For example,
	Given 1->2->3->4, you should return the list as 2->1->4->3.
	Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed.

解题思路：

###  reverseKGroup

前面刚写了 [reverse-nodes-in-k-group](./reverse-nodes-in-k-group.html)，直接调用一下，传参数2即可。

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
ListNode *swapPairs(ListNode *head) 
{
    return reverseKGroup(head, 2);
}
```


###  递归版本


>
	next(p1->p2->p3->p4...) = 	
	p1->next = next(p3->p4...);
	p2->next = p1;
	return p2;

代码如下:

```cpp
ListNode* next(ListNode*p1, ListNode* p2)
{
    if (p1 == NULL) return NULL;
    if (p1 != NULL && p2 == NULL) return p1;
    p1->next = next(p2->next, p2->next ? p2->next->next : NULL);
    p2->next = p1;
    return p2;
}
ListNode *swapPairs(ListNode *head) 
{
    if(head == NULL || head->next == NULL) return head;
    return next(head, head->next);
}
```

###  迭代版本

```cpp
ListNode *swapPairs(ListNode *head) 
{
    if(head == NULL || head->next == NULL) return head;
    //1     2   3       4 5
    //1st   2nd next
    ListNode dummy(-1);
    ListNode *pre = &dummy;
    ListNode *first = head, *second = NULL, *next = NULL;
    while(first && first->next)
    {
        second = first->next;
        next = second->next;
        
        pre->next = second;
        second->next = first;
        first->next = next;
        
        pre = first;
        first = next;
    }
    return dummy.next;
}
```

