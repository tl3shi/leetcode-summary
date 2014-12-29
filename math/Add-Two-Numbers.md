# Add Two Numbers

题目来源：[Add Two Numbers](https://oj.leetcode.com/problems/add-two-numbers/)

>
	You are given two linked lists representing two non-negative numbers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
	Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
	Output: 7 -> 0 -> 8

解题思路：

###  递归版

```cpp
	
	ListNode *addTwoNumbers(ListNode *l1, ListNode *l2, int carry)
	{
	    if(l1 == NULL && l2 == NULL && carry == 0) //only comes the carry,like 5, 5 = 10, or carry = 0
	        return NULL;
	    ListNode * result = new ListNode(carry);
	    if(l1 != NULL)
	        result->val += l1->val;
	    if(l2 != NULL)
	        result->val += l2->val;
	    result->next = addTwoNumbers(l1 == NULL ? NULL : l1->next, l2 == NULL ? NULL : l2->next, result->val / 10);
	    result->val %= 10;
	    return result;
	}
	
	ListNode *addTwoNumbers(ListNode *l1, ListNode *l2)
	{
	    if(l1 == NULL && l2 == NULL)
	        return NULL;
	    if(l1 == NULL)
	        return l2;
	    if(l2 == NULL)
	        return l1;
	    return addTwoNumbers(l1, l2, 0);
	}
```

###  迭代版

```cpp
	
	ListNode *addTwoNumbers(ListNode *l1, ListNode *l2) 
    {
        if(l1 == NULL && l2 == NULL) return NULL;
        if(l1 == NULL || l2 == NULL) return l1 == NULL ? l2 : l1;
        ListNode dummy(-1);
        ListNode * pre = &dummy;
        while(l1 && l2)
        {
            pre->next = new ListNode(l1->val + l2->val);
            pre = pre->next;
            l1 = l1->next;
            l2 = l2->next;
        }
        while(l1){
            pre->next = new ListNode(l1->val);
            pre = pre->next;
            l1 = l1->next;    
        }
        while(l2){
            pre->next = new ListNode(l2->val);
            pre = pre->next;
            l2 = l2->next;    
        }
        pre = dummy.next;
        while(pre){
            int t = pre->val;
            if(t >= 10) {
                pre->val = t % 10; 
                if(pre->next)
                    pre->next->val += t / 10;
                else
                    {pre->next = new ListNode(t / 10); break;}
            }
            pre = pre->next;
        }
        return dummy.next;
    }
```

