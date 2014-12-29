# Merge k Sorted Lists

题目来源：[Merge k Sorted Lists](https://oj.leetcode.com/problems/merge-k-sorted-lists/)

>
	Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
	
解题思路：

跟[merge-two-sorted-lists](./merge-two-sorted-lists.html) 一样, 一个一个merge即可。

```cpp
ListNode * merge2List(ListNode * list1, ListNode* list2)
{
   ListNode dummy(-1);
   ListNode * pre = &dummy;
   while(list1 && list2)
   {
       if(list1->val <= list2->val)
           pre->next = list1, list1 = list1->next;
       else
           pre->next = list2, list2 = list2->next;
       pre = pre->next;
   }
   if(list1)
       pre->next = list1;
   else
       pre->next = list2;
   return dummy.next;
}

ListNode *mergeKLists(vector<ListNode *> &lists) 
{
   if(lists.size() == 0) return NULL;
   ListNode * result = lists[0];
   for(int i = 1; i < lists.size(); i++)
       result = merge2List(result, lists[i]);
   return result;
}
```

不过超时了. 从超时的testcase可以看出,全是短的链表， 加到结果集的链表后，新的短链表加进去运气不好又得将长链表遍历完后才能加到结果链表中。

改成如下代码就可以AC了。

```cpp
ListNode *mergeKLists(vector<ListNode *> &lists) 
{
   if(lists.size() == 0) return NULL;
   vector<ListNode*> merged(lists);
   int size = (int)merged.size();
   while(size > 1)
   {
       for(int i = 0; i < size / 2; i++)
           merged[i] = merge2List(merged[i*2], merged[i*2+1]);
       if((size & 0x1) == 1)
           merged[size / 2 - 1] = merge2List(merged[size / 2 - 1], merged[size-1]);
       size /= 2;
   }
   return merged[0];
}
```


