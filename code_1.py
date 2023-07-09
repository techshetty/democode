t=int(input())
while(t>0):
    n=input()
    f=0
    for i in range(len(n)):
        if int(n[i])==7:
            f=1
            break
    if f==1:
        print("YES")
    else:
        print("NO")
    t-=1