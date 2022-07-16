a=[]
result=[]
while(1):
    a.append(list(map(int,input().rstrip().split())))
    if a[-1][0]==0:
        a.pop()
        break

for j in range(len(a)):
    n=a[j][0]
    k=0
    s=0
    for i in range(1,n):
        if a[j][i]>a[j][i+1]:
                s=max(s,min(a[j][k+1:i+1])*(i-k))
                k=i+1
    s=max(s,min(a[j][k+1:n+1])*(n-k))
            
    result.append(s)
for i in result:
    print(i)
    

        
    



