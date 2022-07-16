import sys
sys.setrecursionlimit(10**6)
T=int(input())
m,cm=[],[]
#벡터 표기법 암기!!!
dx,dy=[1,0,-1,0],[0,1,0,-1]


def dfs(x,y):
    global m,cm
    if cm[x][y]==1:
        return
    cm[x][y]=1
    for i in range(4):
        xx,yy=x+dx[i],y+dy[i]
        if m[xx][yy]==0 or cm[xx][yy]==1:
            continue
        dfs(xx,yy)
def process():
    global m,cm
    M,N,K=map(int,input().split())
    m=[[0 for i in range(50+2)]for _ in range(50+2)]
    cm=[[0 for i in range(50+2)]for _ in range(50+2)]
    for _ in range(K):
        X,Y=map(int,input().split())
        m[Y+1][X+1]=1
    result=0
    for i in range(1,N+1):
        for j in range(1,M+1):
            if m[i][j]== 0 or cm[i][j]==1:
                continue
            dfs(i,j)
            result+=1
    print(result)

for _ in range(T):
    process()
