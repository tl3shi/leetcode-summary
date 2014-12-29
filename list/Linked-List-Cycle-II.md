# Linked List Cycle II

题目来源：[Linked List Cycle II](https://oj.leetcode.com/problems/linked-list-cycle-ii/)

>

    Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

解题思路：

跟[Linked List Cycle 题解](linked-list-cycle.html)一样,运用快慢指针,
先判断是否存在环。然后再找环的起点。
假设存在环，不妨设这个带环的链表长成这个样子(将就看)：

    s-------a->-------
            |        |
            |-<-c----|
如图示，链表起点s,
a是环开始的点，假设快慢指针第一次相遇的点在c处。我们将这个环分为3段，

1. s-->a: 链表起点到还的起点，假设距离为a;
2. a-->c: 环的起点到快慢指针首次相交的点c，设距离为b;
3. c-->a: 快慢指针首次相交的点，再转回环起点a的距离设为c;

那么，得到环的长度为`b+c`, 到快慢指针首次相交时，快/慢指针走的距离设fast/slow分别为：

* fast = a + b + n\*(b + c), n >= 1, (可能快指针比慢指针多走了不止1圈)
* slow = a + b

又因为fast每次走两步，slow每次走一步，所以有 

	fast = 2 * slow 
	a + b + n*(b+c) = 2 * (a+b)
	(n-1)*(b+c) + (b+c) = a+b
	(n-1)*(b+c) + c = a;

观察这个式子，若首次相交时，将fast指针若回到链表头，然后fast、slow都*一步一步走*，那么他们将在哪相遇?

fast走到a时，slow恰好走了(n-1)圈+c，刚好回到了环起点a处。

因此首次相遇后，再次相遇的点即为环的起点。

代码如下：

```cpp

    ListNode *detectCycle(ListNode *head) 
    {
        if(head == NULL || head->next == NULL) return NULL;
        ListNode * fast = head;
        ListNode * slow = head;
        while(fast != NULL && fast->next != NULL)
        {
            fast = fast->next->next;
            slow = slow->next;
            if(fast == slow) //find intersection node
            {
                fast = head;
                while(fast != slow)
                {
                    fast = fast->next;
                    slow = slow->next;
                }
                return fast;
            }
        }
        return NULL;
    }
```

