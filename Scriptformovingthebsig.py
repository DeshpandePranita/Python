import os
import shutil

newpath = r'C:\Users\uie74818\Desktop\New folder (9)'
# if not os.path.exists(newpath):
#     os.makedirs(newpath)

for root, dirs, files in os.walk(r"C:\Users\uie74818\Desktop\EuNCAP2022"):
    for file in files:
        if file.endswith(".bsig"):
             os.path.join(root, file)
             shutil.move(os.path.join(root, file), newpath)
