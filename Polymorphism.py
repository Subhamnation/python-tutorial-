
#%% Polymorphism 

# It provides a way to perform a single action in different forms 
# It is achieved through method overriding and interfaces 

#%% Method Overriding  
# It allows a child class to provide a specific implementation of a method that is already defined in its parent class 

## base Class 1 
class Animal:
    def speak(self):
        return "Sound of the animal"
    
# Derived class 1 
class Dog(Animal):
    def speak(self):
        return "Woof!"
    
#Derived dClass 
class Cat(Animal):
    def speak(self):
        return "Meow!"
#object creation 
dog = Dog()
cat = Cat()
print(dog.speak())
print(cat.speak())

#%% Function that demonstrtes polymorphism 

def animal_speak(animal):
    print(animal.speak())
 
animal_speak(cat)
animal_speak(dog)

#%% POLYMORPHISM with function and methods 
class Shape:
    def area(self):
        return "The area of the figure"
    
#Derived class 1 

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height 
    
    def area(self):
        return self.width * self.height
    
#Derived class 2 

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        
    def area(self):
        return 3.14 * self.radius * self.radius
    
    #Function that generates polymorphism  
def print_area(shape):
    print(f"the area is {shape.area()}")
    
rectangle = Rectangle(4,5)
circle = Circle(3)

print_area(rectangle)
print_area(circle)


    
    
    
    
    
    
    
    
    