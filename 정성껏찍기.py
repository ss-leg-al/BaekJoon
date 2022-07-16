import random

N=int(input())

q=[[0]*(N) for i in range(N)]
matrix=[[0]*(N) for i in range(N)]
for i in range(N):
    matrix[i]=list((map(int,input().split())))
s=0
for i in range(N):
    s+=sum(matrix[i])
