#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Breadth First Traversal for a Graph

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def breadth_first_traversal(self, start):
        visited = [False] * (max(self.graph) + 1)
        queue = []
        
        queue.append(start)
        visited[start] = True
        
        while queue:
            node = queue.pop(0)
            print(node, end=" ")
            
            for neighbor in self.graph[node]:
                if not visited[neighbor]:
                    queue.append(neighbor)
                    visited[neighbor] = True

# Test the code
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

start_node = 2
print("Breadth First Traversal (starting from node {}):".format(start_node))
graph.breadth_first_traversal(start_node)


# In[2]:


# Depth First Traversal for a Graph

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def depth_first_traversal(self, start):
        visited = [False] * (max(self.graph) + 1)
        
        self._dfs(start, visited)
        
    def _dfs(self, node, visited):
        visited[node] = True
        print(node, end=" ")
        
        for neighbor in self.graph[node]:
            if not visited[neighbor]:
                self._dfs(neighbor, visited)

# Test the code
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(1, 2)
graph.add_edge(2, 0)
graph.add_edge(2, 3)
graph.add_edge(3, 3)

start_node = 2
print("Depth First Traversal (starting from node {}):".format(start_node))
graph.depth_first_traversal(start_node)


# In[3]:


# Count the number of nodes at given level in a tree using BFS

from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

def count_nodes_at_level(root, level):
    if root is None:
        return 0

    queue = deque([(root, 0)])  # Initialize queue with root node and its level
    count = 0

    while queue:
        node, node_level = queue.popleft()

        if node_level == level:
            count += 1

        for child in node.children:
            queue.append((child, node_level + 1))

    return count

# Test the code
root = Node(1)
root.children = [Node(2), Node(3), Node(4)]
root.children[0].children = [Node(5), Node(6)]
root.children[1].children = [Node(7)]

level = 2
node_count = count_nodes_at_level(root, level)
print(f"Number of nodes at level {level}: {node_count}")


# In[4]:


# Count number of trees in a forest

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)
        
    def count_trees(self):
        visited = set()
        count = 0
        
        for node in self.graph:
            if node not in visited:
                self._dfs(node, visited)
                count += 1
                
        return count
    
    def _dfs(self, node, visited):
        visited.add(node)
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                self._dfs(neighbor, visited)

# Test the code
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(0, 2)
graph.add_edge(3, 4)
graph.add_edge(5, 6)

tree_count = graph.count_trees()
print("Number of trees in the forest:", tree_count)


# In[5]:


# Detect Cycle in a Directed Graph

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def is_cyclic(self):
        visited = set()
        recursion_stack = set()
        
        for node in self.graph:
            if self._is_cyclic_util(node, visited, recursion_stack):
                return True
            
        return False
    
    def _is_cyclic_util(self, node, visited, recursion_stack):
        visited.add(node)
        recursion_stack.add(node)
        
        for neighbor in self.graph[node]:
            if neighbor not in visited:
                if self._is_cyclic_util(neighbor, visited, recursion_stack):
                    return True
            elif neighbor in recursion_stack:
                return True
            
        recursion_stack.remove(node)
        return False

# Test the code
graph = Graph()
graph.add_edge(0, 1)
graph.add_edge(1, 2)
graph.add_edge(2, 3)
graph.add_edge(3, 0)

has_cycle = graph.is_cyclic()
if has_cycle:
    print("The graph contains a cycle.")
else:
    print("The graph does not contain a cycle.")


# In[9]:


#**Implement n-Queen’s Problem

def is_safe(board, row, col, n):
    # Check if the current position is safe for the queen
    # Check if there is any queen in the same row or same column
    for i in range(n):
        if board[row][i] == 1 or board[i][col] == 1:
            return False

    # Check if there is any queen on the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is any queen on the lower left diagonal
    for i, j in zip(range(row, n, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_n_queens_util(board, col, n):
    # Base case: All queens are placed
    if col >= n:
        return True

    # Recursive case: Try to place the queen in each row of the current column
    for i in range(n):
        if is_safe(board, i, col, n):
            board[i][col] = 1

            # Recur to place the rest of the queens
            if solve_n_queens_util(board, col + 1, n):
                return True

            # If placing the queen doesn't lead to a solution, backtrack
            board[i][col] = 0

    # If no queen can be placed in the current column, return False
    return False

def solve_n_queens(n):
    # Create an empty n x n chessboard
    board = [[0] * n for _ in range(n)]

    # Solve the n-Queens problem
    if solve_n_queens_util(board, 0, n):
        # Print the solution
        for row in board:
            print(' '.join(str(cell) for cell in row))
    else:
        print("No solution exists.")

# Example usage:
n = int(input("Enter the Value : "))
solve_n_queens(n)


# In[ ]:





# In[ ]:




