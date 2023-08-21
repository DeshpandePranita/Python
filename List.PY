"""
items = ['item1','item2','item3']
people = [item.replace('item', 'person') for item in items]
print(people)
"""


list = ['ccrs_OH40','ccrs_OH75', 'ccrs_OH25']
print("Original list ")
print(list)
      
print("After incrementing each element of list by _TV0")  
  
# adding 2 to each value of list
# len method to calculate length of list
# range method is used to go upto a certain range
for i in range( len(list)):
    list[i] = list[i] + '_TV0'
  
print(list)