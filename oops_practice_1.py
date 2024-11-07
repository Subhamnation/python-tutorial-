

#%% 
class Car:
    pass 

audi = Car()
bmw = Car()

print(type(audi))
print(type(bmw))

#%%

print(bmw)
#%% Instance varibles and methods 

class Dog:
    audi.windows = 4
    print(audi.windows)
    
#%% 

tata = Car()
tata.doors = 4
x = dir(tata)

#%% Constructors

class Dog: 
    ## constructor 
    def __init__(self, name, age):
        self.name = name
        self.age = age 
     
## create objects 
dog1 = Dog("Buddy",3)
print(dog1)
print(dog1.name)
print(dog1.age)
    
#%%  Instance Methods 

# Define a class with instance method 
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age 
        
    def bark(self):
        print(f"{self.name} says woof")

dog1 = Dog("Buddy", 3)
dog1.bark()

dog2 = Dog("Lucy", 5)
dog2.bark()

#%% Modelling a bank account

#define a clas for bank account 

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner  = owner
        self.balance = balance 
        
    def deposit(self, amount):
        self.balance+= amount 
        print(f"{amount} is deposited. New balance is {self.balance}")
        
    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient Funds")
        else:
            self.balance-= amount
            print(f"{amount} is withdrawn. New balance is {self.balance}")

#create a bank account 

account = BankAccount("Krish",5000)
print(account.balance)

#Call instance methods 

account.deposit(100)

account.withdraw(300)

#%%
print(account.get_balance())










