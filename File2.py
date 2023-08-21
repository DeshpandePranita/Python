#from File1 import MyClass
import File1
import importlib
def another_function():
    my_instance = File1.MyClass()
    my_instance.my_function()

another_function()
