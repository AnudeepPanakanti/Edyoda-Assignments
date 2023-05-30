#!/usr/bin/env python
# coding: utf-8

# In[2]:


# Write a program to find all pairs of an integer array whose sum is equal to a given number?

def find_pairs(array, target_sum):
    pairs = []
    visited = set()

    for num in array:
        complement = target_sum - num
        if complement in visited:
            pair = (num, complement)
            pairs.append(pair)
        visited.add(num)

    return pairs

# Example usage
nums = [1, 2, 3, 4, 5, 6]
target = int(input("Enter the value : "))

result = find_pairs(nums, target)
print(result)


# In[3]:


# Write a program to reverse an array in place? In place means you cannot create a new array. You have to update the original array.

def reverse_array(array):
    left = 0
    right = len(array) - 1

    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1

# Example usage
nums = [1, 2, 3, 4, 5]
reverse_array(nums)
print(nums)


# In[5]:


# Write a program to check if two strings are a rotation of each other?

def are_rotations(str1, str2):
    if len(str1) != len(str2):
        return False

    concat_str = str1 + str1
    if str2 in concat_str:
        return True
    else:
        return False

# Example usage
string1 = input("Enter the string 1 : ")
string2 = input("Enter the string 2 : ")
result = are_rotations(string1, string2)
print(result)


# In[7]:


# Write a program to print the first non-repeated character from a string?

def first_non_repeated_char(string):
    char_count = {}

    # Count the occurrences of each character
    for char in string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeated character
    for char in string:
        if char_count[char] == 1:
            return char

    # If no non-repeated character is found
    return None

# Example usage
input_string = input("Enter the string : ")
result = first_non_repeated_char(input_string)
print(result)


# In[8]:


# Read about the Tower of Hanoi algorithm. Write a program to implement it.

def tower_of_hanoi(n, source, destination, auxiliary):
    if n > 0:
        # Move n-1 disks from source to auxiliary tower
        tower_of_hanoi(n-1, source, auxiliary, destination)

        # Move the nth disk from source to destination tower
        print(f"Move disk {n} from {source} to {destination}")

        # Move the n-1 disks from auxiliary tower to destination tower
        tower_of_hanoi(n-1, auxiliary, destination, source)


# Example usage
num_disks = 3
tower_of_hanoi(num_disks, 'A', 'C', 'B')


# In[9]:


# Write a program to convert postfix to prefix expression.

def postfix_to_prefix(expression):
    stack = []

    for char in expression:
        if char.isalnum():
            stack.append(char)
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            prefix = char + operand1 + operand2
            stack.append(prefix)

    return stack.pop()

# Example usage
postfix_expression = "ab+c*"
prefix_expression = postfix_to_prefix(postfix_expression)
print(prefix_expression)


# In[11]:


# Write a program to convert prefix expression to infix expression.

def is_operator(char):
    operators = ['+', '-', '*', '/']
    return char in operators

def prefix_to_infix(expression):
    stack = []

    for char in reversed(expression):
        if not is_operator(char):
            stack.append(char)
        else:
            operand1 = stack.pop()
            operand2 = stack.pop()
            infix = f"({operand1}{char}{operand2})"
            stack.append(infix)

    return stack.pop()

# Example usage
prefix_expression = "*+AB-CD"
infix_expression = prefix_to_infix(prefix_expression)
print(infix_expression)


# In[12]:


# Write a program to check if all the brackets are closed in a given code snippet.

def is_matching_pair(opening, closing):
    if opening == '(' and closing == ')':
        return True
    elif opening == '{' and closing == '}':
        return True
    elif opening == '[' and closing == ']':
        return True
    else:
        return False

def are_brackets_balanced(code_snippet):
    stack = []

    for char in code_snippet:
        if char in ['(', '{', '[']:
            stack.append(char)
        elif char in [')', '}', ']']:
            if not stack or not is_matching_pair(stack.pop(), char):
                return False

    if stack:
        return False
    else:
        return True

# Example usage
code = input("Enter the code snippet : ")
result = are_brackets_balanced(code)
print(result)


# In[13]:


# Write a program to reverse a stack.

def reverse_stack(stack):
    if not stack:
        return
    top = stack.pop()
    reverse_stack(stack)
    insert_at_bottom(stack, top)

def insert_at_bottom(stack, item):
    if not stack:
        stack.append(item)
        return
    top = stack.pop()
    insert_at_bottom(stack, item)
    stack.append(top)

# Example usage
stack = [1, 2, 3, 4, 5]
print("Original Stack:", stack)
reverse_stack(stack)
print("Reversed Stack:", stack)


# In[ ]:


# Write a program to find the smallest number using a stack.

class MinStack:
    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, value):
        self.stack.append(value)
        if not self.min_stack or value <= self.min_stack[-1]:
            self.min_stack.append(value)

    def pop(self):
        if not self.stack:
            return None
        value = self.stack.pop()
        if value == self.min_stack[-1]:
            self.min_stack.pop()
        return value

    def get_min(self):
        if not self.min_stack:
            return None
        return self.min_stack[-1]

# Example usage
stack = MinStack()
stack.push(5)
stack.push(3)
stack.push(7)
stack.push(2)

smallest = stack.get_min()
print("Smallest number:", smallest)

