# learn the usage of os
import os

dir_path = '/' # C drive

contents = os.listdir(dir_path) # List all the contents of dir_path

for item in contents:
    print(item)