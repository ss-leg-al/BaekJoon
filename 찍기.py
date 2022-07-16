import copy
import random

N=int(input())

q=[[0]*(N) for i in range(N)]
matrix=[[0]*(N) for i in range(N)]
for i in range(N):
    matrix[i]=list((map(int,input().split())))


for i in range(N):
    for j in range(N):
        q[i][j]=random.randrange(0,10)

for i in range(N):
    for j in range(N):
        print(q[i][j],end=' ')
    print('')




