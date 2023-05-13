#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Problem 1

class Point:

    def __init__(self):
        self.x = x
        self.y = y
        self.z = z

    def sqSum(self):
        pass

print("Enter a Number: ", end="")
num = int(input())
temp = num
sum = 0
while temp!=0:
        rem = temp%10
        sqr = rem*rem
        sum = sum+sqr
        temp = int(temp/10)
print("\nSum of squares of digits of", num, "=", sum)


# In[9]:


#Problem 2
   
class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return self.a+self.b
    def sub(self):
        return self.a-self.b
    def mul(self):
        return self.a*self.b
    def div(self):
        return 0
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
obj=Calculator(a,b)
choice=1
while choice!=0:
    print("0. Exit")
    print("1. Add")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    choice=int(input("Enter choice: "))
    if choice==1:
        print("Result: ",obj.add())
    elif choice==2:
        print("Result: ",obj.sub())
    elif choice==3:
        print("Result: ",obj.mul())
    elif choice==4:
        print("Result: ",round(obj.div(),2))
    elif choice==0:
        print("Exiting!")
    else:
        print("Invalid choice!!")
  
 
print()


# In[11]:


#PROBLEM 3


class Student:
    def __init__(self, name, rollNumber):
        self._name = name
        self._rollNumber = rollNumber
        self._marks = {}

    def getName(self):
        return self._name

    def setName(self, name):
        self._name = name

    def getRollNumber(self):
        return self._rollNumber

    def setRollNumber(self, rollNumber):
        self._rollNumber = rollNumber

    def addMark(self, subject, mark):
        self._marks[subject] = mark

    def getMark(self, subject):
        return self._marks.get(subject)

    def calculateGrade(self):
        total_marks = sum(self._marks.values())
        percentage = total_marks / len(self._marks)

        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        elif percentage >= 60:
            return 'D'
        else:
            return 'F'

    def displayInfo(self):
        print("Student Name:", self._name)
        print("Roll Number:", self._rollNumber)
        print("Marks:")

        for subject, mark in self._marks.items():
            print(subject + ":", mark)

        print("Grade:", self.calculateGrade())


student1 = Student("Steve Rogers", "12345")
student1.addMark("Math", 90)
student1.addMark("Science", 85)
student1.addMark("English", 92)
student1.displayInfo()


# In[12]:


# Problem 4 & 5

class Account:
    def __init__(self, title, balance):
        self.title = title
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into account. New balance: {self.balance}")
        else:
            print("Invalid amount. Deposit amount should be greater than 0.")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                print(f"Withdrew {amount} from account. New balance: {self.balance}")
            else:
                print("Insufficient balance.")
        else:
            print("Invalid amount. Withdrawal amount should be greater than 0.")

    def get_balance(self):
        return self.balance


class SavingsAccount(Account):
    def __init__(self, title, balance, interest_rate):
        super().__init__(title, balance)
        self.interest_rate = interest_rate

    def calculate_interest(self):
        interest = self.balance * (self.interest_rate / 100)
        print(f"Interest calculated: {interest}")
        return interest


account = SavingsAccount("Ashish", 5000, 5)
print(f"Account Holder: {account.title}")
print(f"Initial Balance: {account.get_balance()}")

account.deposit(1000)
account.withdraw(200)
account.calculate_interest()

print(f"Final Balance: {account.get_balance()}")


# In[ ]:




