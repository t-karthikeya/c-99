import os
import shutil
source=input('enter source folder name')
destination=input('enter destination folder name')
source=source + '/'
destination=destination + '/'
files=os.listdir(source)
for file in files:
    shutil.copy((source+file),destination)