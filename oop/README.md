## Decorators

### @classmethod
1. We can call methods without instatiating a class into an object
2. when use? we can instantiate a class, we care about instance attributes and might want to change them (POINT 1)

### @staticmethod
1. similar to @classmethod but do not have access to cls
2. when use? we do not care about instance attributes

## Encapsulation
1. binding of data(variables/attributes) and functions(methods) that manipulate the data into one object so that user or other machines can interact with it (packaging)

## Abstraction
1. hiding away information and give access only to what is necessary
2. when we call a method, we dont care how the code is implemented, the details are hidden from the user 
3. why use? we can work efficiently since we do not need to implement the code from scratch 

### private and public variable
1. users should not have access to modify the instance attributes or methods
2. we put _name to tell other programmers that this is a private variable so please do not touch this but it doesnt enforce it

## Inheritance
1. everything(class, list) in python is an object and it inherits from the python object class
2. why use? avoid repeating code, many children classes can just inherit from a single parent class in order to use the methods
3. if children and parent class both have method with same name, the method in children class will override 

## Polymorphism
1. object classes can share the same method name but they can act differently depends on which object is used


## My thoughts
All the methods and variables are packaged inside the temsorflow library, and all I need to do is just to import the tensorflow library in order to use it (Encapsulation). In order to use the methods I dont need to worry about how the methods are immplemented, I just need to know what the method does (Abstraction)