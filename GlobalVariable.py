"""Variables that are created outside of a function (as in all of the examples above)
are known as global variables.

Global variables can be used by everyone, both inside of functions and outside."""



x="Pranita" #created outside, global variable
def myName():
    print(x) #used inside the function

myName()

###########
x="Pranita"  # created glabal variable 
def myName():
    x="Deshpande" # created inside, local variable same as the global variable
   # Y="Pune"  
#print("My name is" + y)
    print("My surname is" + x) # used within function, can't use outside the function
myName()

print("My name is " + x)

##################  Using Global keyword ################################
""""
The global Keyword
Normally, when you create a variable inside a function, 
that variable is local, and can only be used inside that function.

By using global keyword, we can use local variable outside the function """

def myName():
    global x
    x="Pranita"
    
myName()
print(x)

###########
#To change the value of a global variable inside a function, refer to the variable by using the global

x = "awesome"# global variable

def myfunc():
  global x
  x = "fantastic" #  To change value of x , we make it global. Previous value was awesome and new value is fantastic

myfunc()

print("Python is " + x)