l=[]
r=[]
n=int(input())

for i in range(n):
    k=int(input())
    if k!=0:
        l.append(k)
    elif len(l)==0:
            r.append(0)
    else:
        r.append(max(l))
        l.remove(max(l))
        

for i in r:
    print(i)
