from copy import deepcopy
N=int(input())
b=[list(map(int,input().split()) for i in range(N))]


# 90도 돌리기 암기!!!
def rotate90(Board,N):
    NewBoard=deepcopy(Board)
    for i in range(N):
        for j in range(N):
            NewBoard[j][N-i-1]=Board[i][j]
    return NewBoard

def convert(l,N):
    NewList=[i for i in l if i]
    for i in range(1,len(NewList)):
        if NewList[i-1]==NewList[i]:
            NewList[i-1]*=2
            NewList[i]=0
    return NewList

def dfs(N,Board,count):
    r=max([max(i) for i in Board])
    if count==0:
        return r
    for _ in range(4):
        x=[convert(i,N) for i in Board]
        if x!=Board:
            r=max(r,dfs(N,x,count-1))
        Board=rotate90(Board,N)
    return r
print(dfs(N,b,5))