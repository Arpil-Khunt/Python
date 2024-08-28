import os
#specify the directory path you want to list
directoty_path = "./chapter 1-PS"

#list all file and directory in the specified path
contents = os.listdir(directoty_path)

for item in contents:
    print(item)

