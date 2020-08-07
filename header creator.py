folder=input("Enter folder path: ")
def parser(target_file,destination_file):
    fh = open(target_file)
    ds = open(destination_file,"a")
    for line in fh:
        line=line.strip()
        if line.startswith("#"):
            if line.endswith("\""):
                ds.write(line[line.find('\"')+1:line.find("\"",line.find("\"")+1)]+"\n")#selects till the ' " ' charcter
            elif line.endswith(">"):
                ds.write(line[line.find('<')+1:-1]+"\n") #selects till end of line

import glob
fileList = [f for f in glob.glob(folder+"\\*.c")] + [f for f in glob.glob(folder+"\\*.cpp")]

for file in fileList:
    print()
    parser(file,"headers.h")
print("Creation sucessfull..")
