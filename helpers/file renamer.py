import os
files = os.listdir()
print(files)
for file in files:
    if file.endswith(".txt"):
        newname = file[file.index("(")+1: file.index(")")] + ".txt"
        os.rename(file, newname)