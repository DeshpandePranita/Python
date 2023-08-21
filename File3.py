import sys
sys.path.append("Tutorial")
import File1

import os
path = os.path.abspath("Tutorial")
sys.path.append(path)
import File1

def another_function():
    my_instance = MyClass()
    my_instance.my_function()

another_function()