# Python program to count odd and even numbers of a series

a=eval(input("Enter the numbers : "))

even=0
odd=0
for i in a: 
    if i%2==0: 
        even=even+1
    else: 
        odd=odd+1          
print("Even numbers are : ", even) 
print("Odd numbers are : ", odd)
