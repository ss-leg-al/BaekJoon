
N,M,V=map(int,input().split())
graphmatrix=[[0]*(N+1) for i in range(N+1)]
for i in range(M):
    n1,n2=map(int,input().split())
    graphmatrix[n1][n2]=graphmatrix[n2][n1]=1
dfsvisitedlist=[0]*(N+1)
bfsvisitedlist=[0]*(N+1)

def dfs(V):
    dfsvisitedlist[V]=1
    print(V,end=' ')
    for i in range(1,N+1):
        if dfsvisitedlist[i]==0 and graphmatrix[V][i]==1:
            dfs(i)
def bfs(V):
    queue=[V]
    bfsvisitedlist[V]=1
    while queue:
        V=queue.pop(0)
        print(V,end=' ')
        for i in range(1,N+1):
            if bfsvisitedlist[i]==0 and graphmatrix[V][i]==1:
                queue.append(i)
                bfsvisitedlist[i]=1
dfs(V)
print()
bfs(V)








    
