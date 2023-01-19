#!/usr/bin/env python
# coding: utf-8

# In[14]:


# implement a method that squares passing variables and returns their sum.
class Point:
    
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z

    def display(self):
        print("First element is:",self.x)
        print("Second element is:",self.y)
        print("Third element is:",self.z)
        
    def square(self):
        self.x = self.x**2
        self.y = self.y**2
        self.z = self.z**2
        print("Square of First element is:",self.x)
        print("Square of Second element is:",self.y)
        print("Square of Third element is:",self.z)
        
    def sqSum(self):
        return (self.x+self.y+self.z)
x = int(input("Enter First element:")) 
y = int(input("Enter Second element:")) 
z = int(input("Enter Third element:")) 
p = Point(x,y,z)
print("point object details are:")
p.display()
print("square object details are:")
p.square()
print("sqSum of all the elements is:",p.sqSum())


# In[27]:


#Challenge 2: Implement a Calculator Class
class calculator:
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def add(self):
        return self.num2+self.num1
    def sub(self):
        return self.num2-self.num1
    def multiply(self):
        return self.num2*self.num1
    def divide(self):
        return self.num2/self.num1

obj = calculator(10,94)
print(obj.add())
print(obj.sub())
print(obj.multiply())
print(obj.divide())


# In[112]:


#Challenge3-Implement the complete Student class
class student:
    def __init__(self, name, rollNumber):
        self.__name=name
        self.__rollNumber=rollNumber
        
    #setter method
    def set_name(self,name):
        print("setter method called")
        self.__name=name
        pass
    def get_name(self):
        print("getter method called")
        return self.__name
    pass
    
    
    #setter method
    def set_rollNumber(self,rollNumber):
        self.__rollNumber=rollNumber
        pass
    def get_rollNumber(self):
        return self.__rollNumber
    pass
    
student1 = student("SUDARSHAN","1BM18CV164")
student1.set_name("SUDARSHAN")
print(student1.get_name())
student1.set_rollNumber("1BM18CV164")
print(student1.get_rollNumber())


# In[102]:


#Challenge-4 implement a banking account.
class Account:
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance
class SavingsAccount(Account):
    def __init__(self, title, balance, interestrate):
        super().__init__(title,balance)
        self.interestrate = interestrate
    def interestamount(self):
        print("interest rate:",self.interestrate)
        return self.interestrate
    

a1 = SavingsAccount("Ashish", 5000, 5)
print(a1.title)
print(a1.balance)
print(a1.interestrate) 
        


# In[98]:


#Handling a Bank Account-
import sys
class Account:
    Bank = "INDIAN BANK"
    def __init__(self,title=None,balance=0):
        self.title = title
        self.balance = balance
        
    def deposit(self,deposit):
        self.balance = self.balance+deposit
        print("Balance after deposit is",self.balance)
        return self.balance
    
    def withdraw(self,withdraw):
        if self.balance<withdraw:
            print("Insuffecient Balance in Account")
            sys.exit()
        else:
            self.balance = self.balance-withdraw
            print("Balance after withdraw is",self.balance)
            return self.balance
        
    def get_balance(self):
        return ""
    
class SavingsAccount(Account):
    def __init__(self,title=None,balance=0,interestrate=0):
        super().__init__(title,balance)
        self.interestrate = interestrate
    
    def interestAmount(self):
        self.interestrate = self.interestrate*self.balance/100
        print("Interestrate :",self.interestrate)
        return ""
    
d1 = SavingsAccount("Ashish",2000,5)
print(d1.deposit(500))
d1.withdraw(500)
print(d1.withdraw(500))
print(d1.get_balance())
print(d1.interestAmount())


# In[ ]:




