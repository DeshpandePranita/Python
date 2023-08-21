quote="Hello World"

# == -1 indicates not present 
# != -1 indicates present 

if quote.find("H") == -1:
   print("ok")
else:
    print("pld")


if quote.find("P") == -1: # P is not present in the string
   print("ok")
else:
    print("pld")


if quote.find("H") != -1: # H is present in the string
   print("ok")
else:
    print("pld")

