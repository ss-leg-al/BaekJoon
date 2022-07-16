import copy
import random

N=int(input())
matrix=[[0]*(N) for i in range(N)]
q=[[0]*(N) for i in range(N)]

for i in range(N):
    matrix[i]=list((map(int,input().split())))

def s(k,a,b):
    m=copy.deepcopy(k)
    for i in range(N):
        for j in range(2):
            m[i].insert(0,0)
        for j in range(2):
            m[i].append(0)
    for i in range(2):
        m.insert(0,[0]*(N+4))
        m.append([0]*(N+4))
    r=0
    a+=2
    b+=2
    for i in range(-2,3):
        for j in range(-2,3):
            r+=m[a+i][b+j]
        
    r-=m[a][b]
    return r
def newmatrix(m):
    nm=[[0]*(N) for i in range(N)]
    for i in range(N):
        for j in range(N):
            nm[i][j]=s(m,i,j)
    return nm


while(1):
    g=0
    for i in range(N):
        for j in range(N):
            q[i][j]=random.randrange(0,9)
    for i in range(N):
        for j in range(N):
            if abs(newmatrix(q)[i][j]-matrix[i][j])>((N*N)/2):
                g=1
    if g==0:
        break
    else:
        continue
    
for i in range(N):
    for j in range(N):
        print(q[i][j],end=' ')
    print('')


 