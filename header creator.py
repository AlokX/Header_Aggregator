#folder=input("Enter folder path: ")
def parser(x,y):
    fh = open(x)
    ds = open(y,"a")
    for line in fh:
        line=line.strip()
        if line.startswith("#"):
            if line.endswith("\""):
                ds.write(line[line.find('\"')+1:line.find("\"",line.find("\"")+1)]+"\n")#selects till the '\"' charcter
            elif line.endswith(">"):
                ds.write(line[line.find('<')+1:-1]+"\n") #selects till end of line

import glob
fileList = [f for f in glob.glob("*.c")] + [f for f in glob.glob("*.cpp")]
for file in fileList:
    print()
    parser(file,"headers.h")