n=int(input())
m=[[0 for i in range(n+1)]for j in range(n+1)]


for i in range(1,n+1):
    a=list(map(int,input().split()))
    for j in range(1,i+1):
        m[i][j]=a[j-1]


for i in range(2,n+1):
    for j in range(1,i+1):
        m[i][j]+=max(m[i-1][j-1],m[i-1][j])

print(max(m[-1]))