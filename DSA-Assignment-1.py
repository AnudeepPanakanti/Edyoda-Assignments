#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Delete the elements in an linked list whose sum is equal to zero

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def delete_zero_sum(self):
        dummy = Node(0)  
        dummy.next = self.head
        prefix_sum = 0
        prefix_sums = {}
        current = dummy

        while current:
            prefix_sum += current.data

            if prefix_sum in prefix_sums:
                # Delete elements between the previous node with prefix_sum and the current node
                prev = prefix_sums[prefix_sum]
                prev.next = current.next
            else:
                prefix_sums[prefix_sum] = current

            current = current.next

        self.head = dummy.next

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
llist = LinkedList()
llist.insert(6)
llist.insert(-6)
llist.insert(8)
llist.insert(4)
llist.insert(-12)
llist.insert(9)
llist.insert(8)
llist.insert(-8)
llist.insert(3)

print("Original Linked List:")
llist.display()

llist.delete_zero_sum()

print("Linked List after deleting elements with zero-sum sublists:")
llist.display()


# In[6]:


# Reverse a linked list in groups of given size

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def reverse_in_groups(self, k):
        self.head = self._reverse_in_groups_util(self.head, k)

    def _reverse_in_groups_util(self, head, k):
        if head is None:
            return None

        current = head
        next_node = None
        prev = None
        count = 0

        # Reverse the first k nodes of the linked list
        while current and count < k:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            count += 1

        # Recursively reverse the remaining part of the linked list
        if next_node is not None:
            head.next = self._reverse_in_groups_util(next_node, k)

        return prev

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
llist = LinkedList()
llist.insert(1)
llist.insert(2)
llist.insert(3)
llist.insert(4)
llist.insert(5)
llist.insert(6)
llist.insert(7)
llist.insert(8)

print("Original Linked List:")
llist.display()

k = int(input("Enter the number you want to return in groups of: "))
llist.reverse_in_groups(k)

print(f"Linked List after reversing in groups of {k}:")
llist.display()


# In[7]:


# Merge a linked list into another linked list at alternate positions.

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def merge_alternate(self, other):
        if self.head is None:
            self.head = other.head
            return

        current1 = self.head
        current2 = other.head

        while current1 and current2:
            next1 = current1.next
            next2 = current2.next

            current1.next = current2
            current2.next = next1

            current1 = next1
            current2 = next2

        if current2:
            current1.next = current2

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")


# Example usage:
list1 = LinkedList()
list1.insert(1)
list1.insert(3)
list1.insert(5)

list2 = LinkedList()
list2.insert(2)
list2.insert(4)
list2.insert(6)

print("List 1:")
list1.display()

print("List 2:")
list2.display()

list1.merge_alternate(list2)

print("Merged List:")
list1.display()


# In[9]:


# In an array, Count Pairs with given sum

def count_pairs_with_sum(arr, target_sum):
    count = 0
    complements = {}

    for num in arr:
        complement = target_sum - num
        if complement in complements:
            count += complements[complement]
        if num in complements:
            complements[num] += 1
        else:
            complements[num] = 1

    return count


# Example usage:
array = [1, 5, 7, -1, 5]
target = int(input("Enter the sum value : "))

result = count_pairs_with_sum(array, target)
print(f"Number of pairs with sum {target}: {result}")


# In[10]:


# Find duplicates in an array

def find_duplicates(arr):
    duplicates = []
    seen = set()

    for num in arr:
        if num in seen and num not in duplicates:
            duplicates.append(num)
        else:
            seen.add(num)

    return duplicates


# Example usage:
array = [1, 2, 3, 4, 2, 5, 6, 1, 3]
duplicates = find_duplicates(array)

if duplicates:
    print("Duplicates found:", duplicates)
else:
    print("No duplicates found.")


# In[14]:


# Find the Kth largest and Kth smallest number in an array

def find_kth_largest_smallest(arr, k):
    arr.sort()  # Sort the array in ascending order

    kth_smallest = arr[k-1]
    kth_largest = arr[-k]

    return kth_largest, kth_smallest


# Example usage:
array = [7, 2, 1, 4, 6, 3, 5]
k = int(input("Enter the K value : "))

kth_largest, kth_smallest = find_kth_largest_smallest(array, k)
print(f"The {k} largest number is: {kth_largest}")
print(f"The {k} smallest number is: {kth_smallest}")


# In[15]:


# Move all the negative elements to one side of the array

def move_negative_elements(arr):
    n = len(arr)
    neg_index = 0

    for i in range(n):
        if arr[i] < 0:
            if i != neg_index:
                arr[i], arr[neg_index] = arr[neg_index], arr[i]
            neg_index += 1

    return arr


# Example usage:
array = [4, -1, 8, -3, 2, -7, 6, -5]
result = move_negative_elements(array)
print("Array after moving negative elements to one side:", result)


# In[18]:


# Reverse a string using a stack data structure

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()


def reverse_string(string):
    stack = Stack()
    reversed_string = ""

    # Push each character onto the stack
    for char in string:
        stack.push(char)

    # Pop each character from the stack to reverse the string
    while not stack.is_empty():
        reversed_string += stack.pop()

    return reversed_string


# Example usage:
input_string = input("Enter the string : ")
reversed_string = reverse_string(input_string)
print("Reversed string:", reversed_string)


# In[19]:


# Evaluate a postfix expression using stack

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Cannot pop from an empty stack")
        return self.items.pop()


def evaluate_postfix(expression):
    stack = Stack()

    # Iterate through each character in the expression
    for char in expression:
        if char.isdigit():
            stack.push(int(char))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            result = perform_operation(operand1, operand2, char)
            stack.push(result)

    # The final result will be on top of the stack
    return stack.pop()


def perform_operation(operand1, operand2, operator):
    if operator == '+':
        return operand1 + operand2
    elif operator == '-':
        return operand1 - operand2
    elif operator == '*':
        return operand1 * operand2
    elif operator == '/':
        return operand1 / operand2


# Example usage:
postfix_expression = "532*+"
result = evaluate_postfix(postfix_expression)
print("Result of postfix expression:", result)


# In[ ]:


# Implement a queue using the stack data structure

class Queue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def is_empty(self):
        return len(self.stack1) == 0 and len(self.stack2) == 0

    def enqueue(self, item):
        self.stack1.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("Cannot dequeue from an empty queue")

        if len(self.stack2) == 0:
            while len(self.stack1) > 0:
                self.stack2.append(self.stack1.pop())

        return self.stack2.pop()


# Example usage:
queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())
print("Dequeued item:", queue.dequeue())

