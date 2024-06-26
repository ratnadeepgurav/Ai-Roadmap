# find all files which provided in directory variables
import os

directory = '/'

content = os.listdir(directory)

for item in content:
    print(item)