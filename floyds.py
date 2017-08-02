x=input("Enter a NUmber :")
for i in range(1,x+1) :
    for j in range(1,i+1) :
        print j,
    print
for i in range(-1,x):
    for j in range(1,x-i-1):
        print j,
    print
    
