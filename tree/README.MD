# Tree data structure

A tree collection of entities(nodes) linked together to simulate a hirachy.

## Binary Search Tree(BST)

A binary search tree is a structure in which each node is capable of having two succesor nodes called children. Every key value in ay dode is greater than the key value of its left child and any of its children and less than the key value to its right and any of its children.
Root: the node of a tree structure
Leaf: a node that has no children
Level: the distance of a node from the root
Height(of x): the maximum level/njmber of edges inthe longest path from x to leaf
Depth(of x): number of edges in path from root to x
Maximum number of nodes at any level N is 2^N
A tree with N nodes has exactly N-1 edges

### Binary Search Tree(BST) operations

bool isFull()
bool isEmpty()
