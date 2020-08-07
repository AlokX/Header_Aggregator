def parser(target_file,destination_file):
    fh = open(target_file)
    ds = open(destination_file,"a+")
    for line in fh:
        line=line.strip()
        if line.startswith("#"):
            if line.endswith("\""):
                ds.write(line[line.find('\"')+1:line.find("\"",line.find("\"")+1)]+"\n")#selects till the ' " ' charcter
            elif line.endswith(">"):
                ds.write(line[line.find('<')+1:-1]+"\n") #selects till end of line

import os
import glob
folder_path=input("Enter folder path: ")

if(len(folder_path)<1):
    folder_path=os.getcwd()
#print(folder_path)

fileList = [f for f in glob.glob(folder_path+"\\*.c")] + [f for f in glob.glob(folder_path+"\\*.cpp")]

if not fileList:
    print("No files found!!")
    quit()
for file in fileList:
    print()
    parser(file,folder_path+"\\headers.h")
print("Creation sucessfull..")
