# Python program to print mirror of a word.

word = input("The word is : ")
 
for i in range(len(word) - 1, -1, -1):
  print(word[i],end='')