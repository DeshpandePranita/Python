from importlib import resources
  
# Using the open_text method to open and
# read the resource in the folder
with resources.open_text("texts", "sample.txt") as t:
    txt = t.readlines()
  
# Printing the contents of file
print("".join(txt[:7]))