# Slicing
# Generally,uses square brackets with colon [:] for slicing.

b = "Hello, World!"
print(b[:5])#From the Start till 5 characters

b = "Hello, World!"
print(b[5:])# Takes character till the End except first 5 characters

b = "Hello, World!"
print(b[3:6])

# Use negative indexes to start the slice from the end of the string:
b = "Hello, World!"
print(b[-5:-2])  # From: "o" in "World!" (position -5)
                 # To, but not included: "d" in "World!" (position -2):
###########################################################################################

#Concatination

a="Pranita"
b="deshpande"
c=a+b
print(c)

a="Pranita"
b="deshpande"
c= a + " " + b
print(c)