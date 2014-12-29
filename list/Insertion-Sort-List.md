# Insertion Sort List

题目来源：[Insertion Sort List](https://oj.leetcode.com/problems/insertion-sort-list/)

>Sort a linked list using insertion sort.

解题思路：
发现有逆序的就将这个插入到前面的有序序列里。

```cpp
ListNode *insertionSortList(ListNode *head)
{
    if(NULL == head || NULL == head->next) return head;
    ListNode  result(1);
    result.next = head;
    ListNode * nodei = head;
    while(nodei && nodei->next)
    {
        ListNode * nodej = nodei->next;
        if(nodej->val >= nodei->val)
        {
            nodei = nodei->next;
            continue;
        }
        //insert nodej to result
        ListNode * pos = &result;
        while(pos->next->val < nodej->val)
            pos = pos->next;
        //[pos, pos->next]  -->[pos, nodej, pos->next]
        nodei->next = nodej->next;
        nodej->next = pos->next;
        pos->next = nodej;
    }
    return result.next;
}

```

顺便把选择排序也写下.

```cpp
ListNode * selectionSort(ListNode *head)
{
    ListNode * nodei = head;
    while(nodei)
    {
        ListNode * nodemin = nodei;
        ListNode * nodej = nodei;
        while(nodej)
        {
            if(nodej->val < nodemin->val)
                nodemin = nodej;
            nodej = nodej->next;
        }
        std::swap(nodei->val, nodemin->val);
        nodei = nodei->next;
    }
    return head;
}
```


