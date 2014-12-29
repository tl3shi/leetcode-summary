# LRU Cache

题目来源：[LRU Cache](https://oj.leetcode.com/problems/lru-cache/)

>
Design and implement a data structure for Least Recently Used (LRU) cache. It should support the following operations: get and set.
>
get(key) - Get the value (will always be positive) of the key if the key exists in the cache, otherwise return -1.
set(key, value) - Set or insert the value if the key is not already present. When the cache reached its capacity, it should invalidate the least recently used item before inserting a new item.

解题思路：双向链表 + hashmap

[ref](http://www.cs.uml.edu/~jlu1/doc/codes/lruCache.html)

    Once the data with key K is queried, the function get(K) is first called. 
    If the data of key K is in the cache, the cache just returns the data and refresh the data in the linked list. 
    To refresh data T in the list, we move the item of data T to the head of the list. Otherwise, 
    if the data T of key K is not in the cache, we need to insert the pair into the list. 
    If the cache is not full, we insert into the hash map, and add the item at the head of the list. 
    If the cache is already full, we get the tail of the list and update it with , then move this item to the head of the list.
 
    
[ref1](http://hawstein.com/posts/lru-cache-impl.html)

    LRU的典型实现是hash map + doubly linked list， 双向链表用于存储数据结点，并且它是按照结点最近被使用的时间来存储的。 如果一个结点被访问了，
    我们有理由相信它在接下来的一段时间被访问的概率要大于其它结点。于是， 我们把它放到双向链表的头部。当我们往双向链表里插入一个结点， 我们也有可能很快就会使用到它，
    同样把它插入到头部。 我们使用这种方式不断地调整着双向链表，链表尾部的结点自然也就是最近一段时间， 最久没有使用到的结点。那么，当我们的Cache满了， 
    需要替换掉的就是双向链表中最后的那个结点(不是尾结点，头尾结点不存储实际内容)。
     
    如下是双向链表示意图，注意头尾结点不存储实际内容：
     
    头 --> 结 --> 结 --> 结 --> 尾
    结     点     点     点     结
    点 <-- 1  <-- 2 <-- 3  <-- 点
    假如上图Cache已满了，我们要替换的就是结点3。
 
    哈希表的作用是什么呢？如果没有哈希表，我们要访问某个结点，就需要顺序地一个个找， 时间复杂度是O(n)。使用哈希表可以让我们在O(1)的时间找到想要访问的结点， 
    或者返回未找到。

```cpp
	
	class LRUCache
	{
	public:
	    struct Node
	    {
	        int value;
	        int key;
	        Node * prev;
	        Node * next;
	        Node(int k, int v): key(k),value(v),prev(NULL), next(NULL)
	        {}
	    };
	    
	    LRUCache(int capacity):capacity_(capacity) 
	    {
	        head = new Node(-1,-1);
	        tail = new Node(-1,-1);
	        head->next = tail;
	        tail->prev = head;
	    }
	    
	    ~LRUCache()
	    {
	        delete head;
	        delete tail;
	        for(auto it = kv_.begin(); it!=kv_.end(); it++)
	            delete it->second;
	    }
	    
	    int get(int key) 
	    {
	        auto it = kv_.find(key);
	        if(it != kv_.end())
	        {
	            removeFromList(it->second);
	            move2Head(it->second);
	            return it->second->value;
	        }
	        return -1;
	    }
	    
	    void set(int key, int value) 
	    {
	        auto it = kv_.find(key);
	        if(it != kv_.end())//replace
	        {
	            removeFromList(it->second);
	            it->second->value = value;
	            move2Head(it->second);
	        }else//insert new
	        {
	            if(kv_.size() >= capacity_)//remove tail
	            {
	                auto node = tail->prev;
	                removeFromList(node);//!!Do not forget
	                kv_.erase(node->key);
	                node->key = key;
	                node->value = value;
	                kv_[key] = node;
	                move2Head(node);
	            }else //add
	            {
	                auto node = new Node(key, value);
	                kv_[key] = node;
	                move2Head(node);
	            }
	        }
	    }
	private:
	    Node * head; //head and tail do NOT store data
	    Node * tail;
	    unordered_map<int, Node*> kv_;
	    int capacity_;
	    void removeFromList(Node* node)
	    {
	        node->prev->next = node->next;
	        node->next->prev = node->prev;
	    }
	    void move2Head(Node* node)
	    {
	        Node* old = head->next;
	        old->prev = node;
	        node->next = old;
	        head->next = node;
	        node->prev = head;
	    }
	};
```

看看人家用stl中的list写的，代码多短啊。 ref [leetcode-cpp](https://github.com/soulmachine/leetcode)
list中的方法
>	splice (iterator position, list& x, iterator i);
Transfers elements from x into the container, inserting them at position. [list api](http://www.cplusplus.com/reference/list/list/splice/) 

```cpp

    class LRUCache
    {
    public:
        struct Node
        {
            int value;
            int key;
            Node(int k, int v): key(k),value(v)
            {}
        };
        
        LRUCache(int capacity):capacity_(capacity)
        {
        }
        
        int get(int key)
        {
            auto it = kv_.find(key);
            if(it != kv_.end())
            {
                //transfer: remove it from dataList, add to dataList.begin()
                //std::list::splice http://www.cplusplus.com/reference/list/list/splice/
                dataList.splice(dataList.begin(), dataList, it->second);
                it->second = dataList.begin();
                return it->second->value;
            }
            return -1;
        }
        
        void set(int key, int value)
        {
            auto it = kv_.find(key);
            if(it != kv_.end())//replace
            {
                dataList.splice(dataList.begin(), dataList, it->second);
                it->second = dataList.begin();
                it->second->value = value;
            }else//insert new
            {
                if(kv_.size() >= capacity_)//remove tail
                {
                    kv_.erase(dataList.back().key);
                    auto tail = dataList.back();
                    dataList.pop_back();
                    tail.key = key; tail.value = value;
                    dataList.push_front(tail);
                    kv_[key] = dataList.begin(); //insert
                }else
                {
                    dataList.push_front(Node(key, value));
                    kv_[key] = dataList.begin(); //insert
                }
            }
        }
    private:
        unordered_map<int, list<Node>::iterator> kv_;
        int capacity_;
        list<Node> dataList;
    };
```

