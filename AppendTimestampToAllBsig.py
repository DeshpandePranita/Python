import os
import glob
path = r"C:\Users\uie74818\Desktop\MY_FSF_Bsig"
list_of_bsigs=glob.glob(path+"\\\*.bsig")
print(list_of_bsigs)
for count, i in enumerate(os.listdir(path)):
    dst = f"2022.07.27 22.03.0{str(count)}_" + i
    os.rename(list_of_bsigs[count],r'C:\Users\uie74818\Desktop\folder'+"\\"+dst)
    print(dst)

