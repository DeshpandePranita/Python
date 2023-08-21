lst = [1,3,2,4,5,6,9,8,7,10]
lst.sort()#[1,2,3,4,5,6,7,8,9,10]
first=0
last=len(lst)-1# 9

mid = (first+last)//2 #4

lst[mid]# 5

item = int(input("enter the number to be search"))


found = False

while(first<=last and not found):
    mid = (first + last)//2 #4
    
    if lst[mid] == item:
         print(f"found at location {mid}")#8
         found= True
    else:
        if item < lst[mid]: #
            last = mid - 1
            #print(last)#5
        else:
            first = mid + 1 
            #print(first)#8
  
if found == False:
    print("Number not found")