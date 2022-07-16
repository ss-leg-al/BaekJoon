N=int(input())

r=1
e=11
a=100

while(1):
    if N>=e:
        r+=1
        e+=a
        a*=10
    else:
        print(r)
        break
