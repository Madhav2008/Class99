import os
path = 'C:/Users/Raghav/Desktop/Madhav/New folder (9)/madhav/Python1'
isexist = os.path.exists(path)
print(isexist)
rootext = os.path.splitext(path)
print(rootext)
import shutil
source = "Text1.txt"
destination = "Text2"
dest = shutil.move(source, destination)
print(os.listdir("Text2"))
