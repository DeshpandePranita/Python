
"""
Fruits=["apple", "banana", "chery"]
for x in Fruits:
 print(x)
"""

"""
for x in "banana":
  print(x) #{prints each character from string}
"""

"""
letters=["a","b","c"]
for x in letters:
    print(x)
    if x== "b":
     break    #{a b}
"""
"""
letters=["a","a","c"]
for x in letters:
    if x=="c":
        break #{a a}
    print(x)
"""
"""
letters=["a","b","c"]
for x in letters:
    if x=="b":
       continue #{a c}
    print(x)
"""

# numbers=[1, 2, 3]
# letters=["a", "b" ,"c"]
# for i in numbers:
#     for y in letters:
#         print(i,y)
        

all_events=["pranitad", "pranitad1","prnip"]
for event in all_events:
    if "tad" in event:
        print("ok")
    else:
        print("not present")
