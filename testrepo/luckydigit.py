#Write a programme to accept a date of birth and find the luck digit
x=input("Enter Date:")
y=input("Enter Month:")
z=input("Enter Year:")
total=0
count=x+y+z
l=str(count)
for i in list(l):
    total=total+int(i)
if total>9:
    flist=str(total)
    total=0
    for i in list(flist):
        total+=int(i)
    
print total
