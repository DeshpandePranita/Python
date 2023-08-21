import os
list = os.listdir(r"C:\Users\uie74818\Desktop\MY_FSF_Bsigs")
for count, i in enumerate (os.listdir(r"C:\Users\uie74818\Desktop\MY_FSF_Bsigs")):
    dst = f"2022.07.27 22.03.0{str(count)}_" + i
    print(dst)
