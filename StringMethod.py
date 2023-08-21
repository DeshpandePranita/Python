name="India"#define strings
print(name.upper())
print(name.find("a"))#gives position
print(name.replace("I", "p"))
print('d' in name)#if exist then prints true

name1=' pranita'
print(name1.strip())#The strip() method removes any whitespace from the beginning or the end: like 'pranita'########################################################################################

#Format Method
""" we can combine strings and numbers by using the format() method!
The format() method takes the passed arguments, formats them, 
and places them in the string where the placeholders {} are:
"""
quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))

#You can use index numbers {0} to be sure the arguments are placed in the correct placeholders:
quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))