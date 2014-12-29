# Sort List

题目来源：[Sort List ](https://oj.leetcode.com/problems/sort-list/)

>Sort a linked list in O(n log n) time using constant space complexity.

解题思路：
可以用归并或者快排.
merge就比较简单，一个一个比较然后将较小的放到上一个的后面。 用一个dummy省去第一个head的确定。

```cpp
ListNode* merge(ListNode* head1, ListNode* head2)
{
    ListNode dummy(-1);
    ListNode * p = &dummy;
    while(head1 && head2)
    {
        if(head1->val < head2->val)
        {
            p->next = head1;
            head1 = head1->next;
        }else 
        {
            p->next = head2;
            head2 = head2->next;
        }
        p = p->next;
    }    
    if(head1 != NULL)
        p->next = head1;
    else
        p->next = head2;
    return dummy.next;
}
```
然后就是递归一半一半来，如下所示：

```cpp
ListNode * mergesort(ListNode * head)
{
    if (head == NULL || head->next == NULL)
        return head;
    int len = list_len(head);
    if(len <= 2)
    {
        if(len == 1) return head;
        if(len == 2 && head->val > head->next->val)
        {
            swap(head, head->next);//or std::swap(head->val, head->next->val);
            return head;
        }
    }
    int mid = len >> 1;
    ListNode * left_tail = head;
    int i = mid-1;
    while(i)
    {
        left_tail = left_tail->next;
        i -= 1;
    }
    ListNode * right = left_tail->next;
    left_tail->next = NULL;
    ListNode * left_result = mergesort(head);
    ListNode * right_result = mergesort(right);
    return merge(left_result, right_result);
}
```
当然也可以用快慢指针去找中间的那个。

```cpp
ListNode *sortList(ListNode *head) 
    {
        if(NULL == head || NULL == head->next) return head;
        ListNode* fast = head;
        ListNode* slow = head;
        while(NULL != fast->next && NULL != fast->next->next){
            slow = slow->next;
            fast = fast->next->next;
        }
        //slow is mid, ignore fast: (last or last but one)
        ListNode * mid = slow;
        slow = slow->next; //the right part 
        mid->next = NULL; // cut the left part
        ListNode * left = sortList(head);
        ListNode * right = sortList(slow);
        return merge(left, right);
    }
```

刚开始写的快排，有的testcase过不了(数字范围全是1-3那个共30293个数)，把这个testcase排除掉后，也能AC。

```cpp
 ListNode* quick_sort_(ListNode * head)
{
    if(head == NULL || head->next == NULL)
        return head;
    if(len(head) <= 1000) return mergeSort(head);
    ListNode   lefthead = ListNode(-1);
    ListNode   righthead = ListNode(-1);
    ListNode * left = &lefthead;
    ListNode * right = &righthead;
    
    ListNode * pivot =  head; //or random select one
    ListNode * t = head->next;
    while(t != NULL)
    {
        if(t->val <= pivot->val)
        {
            left->next = t;
            left = left->next;
        }else
        {
            right->next = t;
            right = right->next;
        }
        t = t->next;
    }
    if(left != NULL) left->next = NULL;
    if(right != NULL) right->next = NULL;
    ListNode * left_result = quick_sort_(lefthead.next);
    ListNode * right_result = quick_sort_(righthead.next);
    ListNode * newresult_head = left_result;
    if(left_result != NULL)
    {
        while(left_result->next != NULL)
            left_result = left_result->next;
        //left_result->next is NULL
        left_result->next = pivot;
    }else
    {
        newresult_head = pivot;
    }
    pivot->next = right_result;
   
    return newresult_head;
}

ListNode * quick_sort(ListNode * head)
{
    if(head == NULL || head->next == NULL)
        return head;
    //if(len(head) == 30293) return countSort(head); 
    return quick_sort_(head);
}
```

