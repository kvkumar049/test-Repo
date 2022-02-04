#Write a program to find the correct string and calculate the score
x=['tca','dfni','sbos','sfta']

cnt=0
for i in x:
    l=raw_input("Enter a string :")
    if l=='cat':
        cnt=cnt+1
    elif l=='find':
        cnt=cnt+1
    elif l=='boss':
        cnt=cnt+1
    elif l=='fast':
        cnt=cnt+1
if cnt<1:
    print "Oops! You are Looser, Better luck Nexttime.Score is :",cnt
else:
    print  "Well done! Your Score is:",cnt
  



