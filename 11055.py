from copy import deepcopy
N,l=int(input()),list(map(int,input().split()))

dp=deepcopy(l)

for i in range(1,N):
    for j in range(i):
        if l[i]>l[j]:
            dp[i]=max(dp[j]+l[i],dp[i])
print(max(dp))