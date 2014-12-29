# Clone Graph

题目来源：[Clone Graph](https://oj.leetcode.com/problems/clone-graph/)

>

	Clone an undirected graph. Each node in the graph contains a label and a list of its neighbors.
	
	
	OJ's undirected graph serialization:
	Nodes are labeled uniquely.
	
	We use # as a separator for each node, and , as a separator for node label and each neighbor of the node.
	As an example, consider the serialized graph {0,1,2#1,2#2,2}.
	
	The graph has a total of three nodes, and therefore contains three parts as separated by #.
	
	First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
	Second node is labeled as 1. Connect node 1 to node 2.
	Third node is labeled as 2. Connect node 2 to node 2 (itself), thus forming a self-cycle.
	Visually, the graph looks like the following:
	
	       1
	      / \
	     /   \
	    0 --- 2
	         / \
	         \_/


解题思路：

用BFS+hashmap解决。

```cpp

	//Definition for undirected graph.
	struct UndirectedGraphNode 
	{
		int label;
		vector<UndirectedGraphNode *> neighbors;
		UndirectedGraphNode(int x) : label(x) {};
	};
 
	UndirectedGraphNode *cloneGraph(UndirectedGraphNode *node) 
    {
        if(node == NULL) return NULL;
        unordered_map<UndirectedGraphNode*, UndirectedGraphNode*> copies;
        queue<UndirectedGraphNode*> todo; 
        todo.push(node);
        copies[node] = new UndirectedGraphNode(node->label);
        while(!todo.empty())
        {
            auto origin = todo.front(); todo.pop();
            UndirectedGraphNode* cpy = copies[origin];
            for(auto it = origin->neighbors.begin(); it != origin->neighbors.end(); it++)
            {
                if(copies.find(*it) == copies.end())
                {
                    auto node1 = new  UndirectedGraphNode((*it)->label);    
                    copies[*it] = node1;
                    todo.push(*it);
                }
                cpy->neighbors.push_back(copies[*it]);
            }
        }
        return copies[node];
    }
```

