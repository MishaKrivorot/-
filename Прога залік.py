f=open("time.txt", "rt")
a=int(input("введіть певне значення у форматі ААА: "))
if a>999 or a<100:
    while a>999 or a<100:
        a = int(input("невірно задане значення, введіть певне значення у форматі ААА: "))
for i in f:
    x=i.find(" ")
    x+=1
    y=""
    for j in range(x,len(i)-1):
        y+=i[j]
    if int(y)>a:
        print("Час при якому введене значення менше за задані: " + i[0:x])
