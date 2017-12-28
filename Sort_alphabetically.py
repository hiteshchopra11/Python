import re
import sys

if sys.version_info<(3,0):
    op=raw_input("Enter the filename\n")
else:
    op=input("Enter the filename\n")
fileopen=open(op,"r")
newfile=open('sorted.txt',"w")
lines= fileopen.readlines()
c=0
for line in lines:
    c=c+1
    blank= re.sub("\d+\.\ ?","",line)  
    if blank.startswith(" "):
        blank=blank.replace(" ","")
    newfile.write(blank)
    #print blank
newfile.close()

my_file=open("sorted.txt","r")
lines=my_file.readlines()
lines.sort()
my_file.close()
my_file=open("sorted.txt","w")
c=0
for line in lines:
    c=c+1
    print(('%d. %s')%(c,line))
    final=(('%d. %s')%(c,line)) 
    my_file.write(final)
my_file.close()
   


