# Copy List with Random Pointer

题目来源：[Copy List with Random Pointer](https://oj.leetcode.com/problems/copy-list-with-random-pointer/)

>

    A linked list is given such that each node contains an additional random
    pointer which could point to any node in the list or null.

    Return a deep copy of the list.

```cpp
    
    struct RandomListNode 
    {
        int label;
        RandomListNode *next, *random;
        RandomListNode(int x) : label(x), next(NULL), random(NULL) {}
    };
```

解题思路：

###  传统方法用hashmap


主要是解决random pointer的问题，可以用一个map把copy过的存起来，下次碰到的时候直接从map中取。

```cpp
    RandomListNode *copyRandomListUseMap(RandomListNode *head)
    {
        unordered_map<RandomListNode*, RandomListNode*> copyed;
        RandomListNode * head1 = new RandomListNode(head->label);
        copyed[head] = head1;
        RandomListNode * headbak = head1;
        //node's next can not construct a cycle.
        while(head)
        {
            if(head->next){
                if (copyed.find(head->next) != copyed.end())
                    head1->next = copyed[head->next];
                else
                {
                    head1->next = new RandomListNode(head->next->label); 
                    copyed[head->next] = head1->next;
                }
            } 
            if(head->random){
                if (copyed.find(head->random) != copyed.end())
                    head1->random =  copyed[head->random];
                else
                {
                    head1->random = new RandomListNode(head->random->label);
                    copyed[head->random] = head1->random;    
                }
            }
            head = head->next;
            head1 = head1->next;
        }
        return headbak;
    }
    
    RandomListNode *copyRandomList(RandomListNode *head) 
    {
        if(head == NULL) return NULL;
        return copyRandomListUseMap(head);
    }

```

###  常数空间神奇妙解

上面的的方法用了额外的空间，网上总是有些高人能想出牛B的解法。下面就是一个。

[不用map等数据结构常数空间解Copy List with Random Pointer](http://crushbeercrushcode.org/2013/09/copying-linked-lists-with-random-pointers)，该方法分3步：

     1. 直接遍历原链表，copy一遍，random指向跟原来一样的node。将copy的node0插入到原来链表的node0和node1之间,copy的node1插入原来node1和node2之间，依次类推。
     2. 根据第一步有，nodei->next是node的copy的那个(i为偶数)，现在要解决copy的node的random问题，即 nodei->next的random＝? 其实有`nodei->next->random = nodei->random->next`; nodei->random是原来的random，其next就是copyed的原来random的拷贝。 这步很关键。
     3. 将这个连接在一起的链表分开，注意要断开。 

![常数空间解Copy List with Random Pointer](http://tl3shi.github.io/resource/blogimage/leetcode-copy-list-with-random.jpg)

举例个例子, 上面的一排数据1,2,3,4原始数据前后通过next连接, 然后1和2的random指针分别指向3和4.

第1步,copy并把copy得到的数据放到原来的后面.得到下一排数据.

然后观察, 1->next->random = ? 即 copy得到的蓝色1的random指针应该指向哪? 其实就是原来的黑色1->random(黑色3)->next(蓝色3),即`nodei->next->random = nodei->random->next`

第3步,再断开，得到copy后的链表。

AC代码如下:

```cpp

	RandomListNode *copyRandomListConstantSpace(RandomListNode *head)
    {
        RandomListNode * src = head;
        while(src)
        {
            RandomListNode* copy = new RandomListNode(src->label);
            copy->random = src->random;
            //insert between src, src->next;
            auto next = src->next;
            copy->next = next;
            src->next = copy;
            src = next;
        }
        //step 2, deal with random pointer
        src = head;
        while(src)
        {
        	//src->next is the copyed one, src->random->next is the copied src->random
            src->next->random = src->random == NULL ? NULL : src->random->next;
            src = src->next->next;//src->next is surely not NULL
        }
        //split
        src = head;
        auto result = src->next;
        auto cpy = result;
        while(src->next)
        {
            src->next = src->next->next;
            src = src->next;
            if(src == NULL) break;
            cpy->next = cpy->next->next;
            cpy = cpy->next;
        }
        return result;
    }

```

