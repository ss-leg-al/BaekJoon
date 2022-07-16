a=input()
b=input()
la=len(a)
lb=len(b)
c=[[0]*(lb+1) for i in range(la+1)]

for i in range(1,la+1):
    for j in range(1,lb+1):
        if a[i-1]==b[j-1]:
            c[i][j]=c[i-1][j-1]+1
        else:
            c[i][j]=max(c[i-1][j],c[i][j-1])
print(c[i][j])