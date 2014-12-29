# Reorder List

题目来源：[Reorder List](https://oj.leetcode.com/problems/reorder-list/)

>

    Given a singly linked list L: L0→L1→…→Ln-1→Ln,
    reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

    You must do this in-place without altering the nodes' values.

    For example,
    Given {1,2,3,4}, reorder it to {1,4,2,3}.


解题思路：

###  `O(n)`时间 + `O(n)`空间

将node都copy出来放到数组里，后半段逆序(或者直接通过下标不用逆序)连接前半段。

```cpp

	//O(n) + O(n)
	void reorderList2(ListNode* head)
	{
	    vector<ListNode*> nodes;
	    while(head)
	    {
	        nodes.push_back(head);
	        head = head->next;
	    }
	    int n = (int)nodes.size();
	    int mid = n >> 1;
	    std::reverse(nodes.begin()+mid, nodes.end());
	    for(int i = 0; i < mid; i++)
	    {
	        nodes[i]->next = nodes[i+mid];
	        nodes[i+mid]->next = nodes[i+1];
	    }
	    if((n & 0x1) == 0x1)//odd 0,1,2,3,4 | 0,1,4,3,2 | 0->4->1->3->4 ==>0->4->1->3->2->NULL
	    {
	        nodes[n-2]->next = nodes[n-1];
	        nodes[n-1]->next = NULL;
	    }//even 0,1,2,3 | 0,1,3,2| 0->3->1->2
	    else
	        nodes[n-1]->next = NULL;
	}
```

###  `O(n)`时间 + `O(1)`空间

这才是出题者的意图，同样后半段逆序，但通过指针的方式就地逆序，然后与前半段连接。

```cpp

	ListNode * reverseList(ListNode * head)
	{
	    if(head == NULL) return NULL;
	    ListNode * pre = head;
	    ListNode * node = head->next;
	    while(node){
	        ListNode* next = node->next;
	        node->next = pre;
	        pre = node;
	        node = next;
	    }
	    head->next = NULL; //!!Do not forget
	    return pre;
	}
	
	//O(n) time + O(1) space
	void reorderList(ListNode *head)
	{
	    if(head == NULL || head->next == NULL) return ;
	    
	    ListNode * first = head;
	    ListNode * fast = head;
	    while(fast != NULL && fast->next != NULL)
	    {
	        fast = fast->next->next;
	        head = head->next;
	    }
	    ListNode * second = head->next;
	    head->next = NULL;
	    second = reverseList(second);
	    
	    while(second != NULL)
	    {
	        ListNode * tmp = second->next;
	        second->next = first->next;
	        first->next = second;
	        first = first->next->next;
	        second = tmp;
	    }
	}
```

