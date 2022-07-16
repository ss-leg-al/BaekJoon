n=int(input())
a=[]
a=list(map(int,input().rstrip().split()))
b=list(map(int,input().rstrip().split()))
cost=0
for i in range(1,n):
    cost+=min(b[:i])*a[i-1]
print(cost)
        