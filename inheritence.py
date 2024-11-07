
#%% Inheritence 

## parent Class 
class Car:
    def __init__(self, windows, doors, enginetype):
        self.windows = windows
        self.doors = doors 
        self.enginetype = enginetype
        
    def drive(self):
        print(f"The Person will drive the {self.enginetype} car")
        
#%% 
car1= Car(4,5, "petrol")
car1.drive()

#%% Single Inheritence 

class Tesla(Car):
    def __init__(self, windows, doors, enginetype, is_selfdriving):
        super().__init__(windows, doors, enginetype)
        self.is_selfdriving = is_selfdriving
        
    def selfdriving(self):
        print(f"Tesla supports self driving: {self.is_selfdriving}")

# Assuming a definition for the Car class is present
tesla1 = Tesla(4, 5, "electric", True)
tesla1.selfdriving()

#%% Multiple Inheritence 
# When a class inherits more than one base class 

class Animal: 
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        print("Subclass must implement this method")
        
# Base class 2 
class Pet:
    def __init__(self, owner):
        self.owner = owner 
        
# Derived class 
class Dog(Animal, Pet):
    def __init__(self, name, owner):
        Animal.__init__(self, name)  # Fixed: added parentheses
        Pet.__init__(self, owner)    # Fixed: added parentheses
    
    def speak(self):
        return f"{self.name} says woof"
    
# Create an object 
dog = Dog("Buddy", "Krish")
print(dog.speak())
print(f"Owner: {dog.owner}")








