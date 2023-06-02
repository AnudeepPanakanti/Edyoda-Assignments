#!/usr/bin/env python
# coding: utf-8

# In[1]:


# BINARY TREE

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            self._insert_recursive(data, self.root)

    def _insert_recursive(self, data, node):
        if data < node.data:
            if node.left is None:
                node.left = Node(data)
            else:
                self._insert_recursive(data, node.left)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self._insert_recursive(data, node.right)

    def search(self, data):
        return self._search_recursive(data, self.root)

    def _search_recursive(self, data, node):
        if node is None or node.data == data:
            return node
        if data < node.data:
            return self._search_recursive(data, node.left)
        else:
            return self._search_recursive(data, node.right)

    def delete(self, data):
        self.root = self._delete_recursive(data, self.root)

    def _delete_recursive(self, data, node):
        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_recursive(data, node.left)
        elif data > node.data:
            node.right = self._delete_recursive(data, node.right)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self._find_minimum(node.right)
                node.data = temp.data
                node.right = self._delete_recursive(temp.data, node.right)
        return node

    def _find_minimum(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        if node:
            self._inorder_recursive(node.left)
            print(node.data, end=" ")
            self._inorder_recursive(node.right)

    def preorder_traversal(self):
        self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        if node:
            print(node.data, end=" ")
            self._preorder_recursive(node.left)
            self._preorder_recursive(node.right)

    def postorder_traversal(self):
        self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        if node:
            self._postorder_recursive(node.left)
            self._postorder_recursive(node.right)
            print(node.data, end=" ")


# Example usage
tree = BinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(6)
tree.insert(9)

print("Inorder traversal:")
tree.inorder_traversal()
print("\nPreorder traversal:")
tree.preorder_traversal()
print("\nPostorder traversal:")
tree.postorder_traversal()

print("\nSearch for 6:")
result = tree.search(6)
if result:
    print("Element found in the tree.")
else:
    print("Element not found in the tree.")

print("\nDelete 4 from the tree.")
tree.delete(4)
print("Inorder traversal after deletion:")
tree.inorder_traversal()


# In[2]:


# HEIGHT OF A GIVEN BINARY TREE

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def tree_height(node):
    if node is None:
        return 0
    else:
        left_height = tree_height(node.left)
        right_height = tree_height(node.right)

        # Return the maximum height between the left and right subtrees
        return max(left_height, right_height) + 1

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

height = tree_height(root)
print("Height of the tree is:", height)


# In[3]:


# Perform Pre-order, Post-order, In-order traversal

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def pre_order_traversal(node):
    if node:
        print(node.data, end=" ")
        pre_order_traversal(node.left)
        pre_order_traversal(node.right)

def in_order_traversal(node):
    if node:
        in_order_traversal(node.left)
        print(node.data, end=" ")
        in_order_traversal(node.right)

def post_order_traversal(node):
    if node:
        post_order_traversal(node.left)
        post_order_traversal(node.right)
        print(node.data, end=" ")

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Pre-order traversal:")
pre_order_traversal(root)

print("\nIn-order traversal:")
in_order_traversal(root)

print("\nPost-order traversal:")
post_order_traversal(root)


# In[4]:


# Function to print all the leaves in a given binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_leaves(node):
    if node is None:
        return
    
    if node.left is None and node.right is None:
        print(node.data, end=" ")

    print_leaves(node.left)
    print_leaves(node.right)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)

print("Leaves of the binary tree:")
print_leaves(root)


# In[5]:


# Implement BFS (Breath First Search) and DFS (Depth First Search)

from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, u, v):
        if u not in self.graph:
            self.graph[u] = []
        self.graph[u].append(v)

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            if vertex in self.graph:
                for neighbor in self.graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
                        visited.add(neighbor)

    def dfs(self, start):
        visited = set()
        self._dfs_recursive(start, visited)

    def _dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        if vertex in self.graph:
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    self._dfs_recursive(neighbor, visited)

# Example usage
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

print("BFS traversal:")
graph.bfs(2)
print("\nDFS traversal:")
graph.dfs(2)


# In[6]:


# Find sum of all left leaves in a given Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def sum_left_leaves(node):
    if node is None:
        return 0

    # Check if the left child is a leaf node
    if node.left and node.left.left is None and node.left.right is None:
        left_leaf_sum = node.left.data
    else:
        left_leaf_sum = sum_left_leaves(node.left)

    right_leaf_sum = sum_left_leaves(node.right)

    return left_leaf_sum + right_leaf_sum

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)
root.right.right.left = Node(8)

total_sum = sum_left_leaves(root)
print("Sum of all left leaves:", total_sum)


# In[7]:


# Find sum of all nodes of the given perfect binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def get_sum(node):
    if node is None:
        return 0

    return node.data + get_sum(node.left) + get_sum(node.right)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

total_sum = get_sum(root)
print("Sum of all nodes:", total_sum)


# In[8]:


# Count subtress that sum up to a given value x in a binary tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def count_subtrees_with_sum(node, target_sum):
    if node is None:
        return 0

    count = count_subtrees_with_sum(node.left, target_sum) + count_subtrees_with_sum(node.right, target_sum)

    current_sum = node.data + sum_of_subtree(node.left) + sum_of_subtree(node.right)

    if current_sum == target_sum:
        count += 1

    return count

def sum_of_subtree(node):
    if node is None:
        return 0

    return node.data + sum_of_subtree(node.left) + sum_of_subtree(node.right)

# Example usage
root = Node(5)
root.left = Node(-3)
root.right = Node(2)
root.left.left = Node(4)
root.left.right = Node(7)
root.right.left = Node(6)
root.right.right = Node(5)

target_sum = 9
subtree_count = count_subtrees_with_sum(root, target_sum)
print("Number of subtrees with sum", target_sum, ":", subtree_count)


# In[9]:


# Find maximum level sum in Binary Tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def max_level_sum(root):
    if root is None:
        return 0

    queue = [root]
    max_sum = float('-inf')

    while queue:
        level_sum = 0
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.pop(0)
            level_sum += node.data

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        max_sum = max(max_sum, level_sum)

    return max_sum

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.right = Node(6)
root.right.right.left = Node(8)

max_sum = max_level_sum(root)
print("Maximum level sum:", max_sum)


# In[10]:


# Print the nodes at odd levels of a tree

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def print_odd_level_nodes(node, level):
    if node is None:
        return

    if level % 2 != 0:
        print(node.data, end=" ")

    print_odd_level_nodes(node.left, level + 1)
    print_odd_level_nodes(node.right, level + 1)

# Example usage
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

print("Nodes at odd levels:")
print_odd_level_nodes(root, 1)


# In[ ]:




