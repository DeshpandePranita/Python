def my(type:str, warn:bool, info:bool):
 #status="ok"
 type="3"
 warn=True
 info=True

 if type=="3":
    if (warn is True) and (info is True):
        print("pass")
    else:
       print("ok")
 else:
       print("g")

 return my()

   