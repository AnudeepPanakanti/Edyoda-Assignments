#!/usr/bin/env python
# coding: utf-8

# In[5]:


#PROBLEM 1-A


{
  "employees": [
    {
      "Name": "John Doe",
      "DOB": "1990-05-15",
      "Height": 175,
      "City": "New York",
      "State": "NY"
    },
    {
      "Name": "Steve Smith",
      "DOB": "1985-08-25",
      "Height": 162,
      "City": "Los Angeles",
      "State": "CA"
    },
    {
      "Name": "Marcus",
      "DOB": "1992-03-10",
      "Height": 180,
      "City": "Chicago",
      "State": "IL"
    },
    {
      "Name": "Edward Lewis",
      "DOB": "1993-11-28",
      "Height": 168,
      "City": "Houston",
      "State": "TX"
    },
    {
      "Name": "David Dead",
      "DOB": "1988-09-06",
      "Height": 170,
      "City": "San Francisco",
      "State": "CA"
    }
  ]
}


# In[12]:


import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

# Read the JSON file
with open('Employee.json') as file:
    data = json.load(file)

# Create a list to store Employee objects
employees = []

# Iterate over each employee in the JSON data
for employee_data in data['employees']:
    name = employee_data['Name']
    dob = employee_data['DOB']
    height = employee_data['Height']
    city = employee_data['City']
    state = employee_data['State']

    # Create an Employee object and add it to the list
    employee = Employee(name, dob, height, city, state)
    employees.append(employee)

# Print the list of Employee objects
for employee in employees:
    print(f"Name: {employee.name}")
    print(f"DOB: {employee.dob}")
    print(f"Height: {employee.height}")
    print(f"City: {employee.city}")
    print(f"State: {employee.state}")
    print()


# In[2]:


#PROBLEM 1-B


import json

states_and_capitals = {
    "Andhra Pradesh": "Hyderabad",
    "Assam": "Dispur",
    "Bihar": "Patna",
    "Gujarat": "Gandhinagar",
    "Karnataka": "Bengaluru",
    "Maharashtra": "Mumbai",
    "Rajasthan": "Jaipur"
}

# Writing the dictionary into JSON
with open("indian_states.json", "w") as file:
    json.dump(states_and_capitals, file)


# In[9]:


#PROBLEM 2


class Dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"Dog name: {self.name}")
        print(f"Age: {self.age}")

    def get_info(self):
        print(f"Coat color: {self.coat_color}")


class JackRussellTerrier(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def fetch_ball(self):
        print(f"{self.name} is fetching the ball.")

    def hunt(self):
        print(f"{self.name} is hunting.")


class Bulldog(Dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def guard_house(self):
        print(f"{self.name} is guarding the house.")

    def drool(self):
        print(f"{self.name} is drooling.")


# Creating objects and implementing the functionalities
dog1 = Dog("Max", 3, "Brown")
dog1.description()
dog1.get_info()
print()

dog2 = JackRussellTerrier("Buddy", 5, "White and Brown")
dog2.description()
dog2.get_info()
dog2.fetch_ball()
dog2.hunt()
print()

dog3 = Bulldog("Rocky", 4, "Fawn")
dog3.description()
dog3.get_info()
dog3.guard_house()
dog3.drool()


# In[ ]:




