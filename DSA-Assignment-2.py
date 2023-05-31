#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BINARY SEARCH

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


# Example usage
sorted_list = [2, 4, 7, 10, 15, 20, 22]
target_value = 10

result = binary_search(sorted_list, target_value)

if result != -1:
    print(f"Element {target_value} found at index {result}.")
else:
    print("Element not found.")


# In[2]:


#QUICK SORT

def quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


# Example usage
unsorted_list = [6, 2, 9, 1, 5, 3, 8, 4, 7]
sorted_list = quick_sort(unsorted_list)

print("Sorted list:", sorted_list)


# In[3]:


#MERGE SORT

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

    # Recursively sort the two halves
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Merge the sorted halves
    return merge(left_half, right_half)


def merge(left, right):
    merged = []
    left_index = right_index = 0

    # Merge the two halves by comparing elements
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    # Append remaining elements, if any
    merged.extend(left[left_index:])
    merged.extend(right[right_index:])

    return merged


# Example usage
unsorted_list = [6, 2, 9, 1, 5, 3, 8, 4, 7]
sorted_list = merge_sort(unsorted_list)

print("Sorted list:", sorted_list)


# In[4]:


# INSERTION SORT

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# Example usage
unsorted_list = [6, 2, 9, 1, 5, 3, 8, 4, 7]
insertion_sort(unsorted_list)

print("Sorted list:", unsorted_list)


# In[5]:


# SORTING OF STRING

def sort_strings(string_list):
    sorted_list = sorted(string_list)
    return sorted_list


# Example usage
unsorted_list = ["banana", "apple", "cherry", "date", "kiwi"]
sorted_list = sort_strings(unsorted_list)

print("Sorted list:", sorted_list)


# In[ ]:




