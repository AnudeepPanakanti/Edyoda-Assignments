# Program to display the Fibonacci sequence

x=int(input("Enter the number of terms : "))
n1=0
n2=1
count=0
if x==0:
   print("Fibonacci sequence : ")
   print(n1)
elif x<=0:
    print("Enter positive numbers")
else:
   print("Fibonacci sequence:")
   while count < x:
       print(n1)
       y= n1 + n2
       n1 = n2
       n2 = y
       count += 1