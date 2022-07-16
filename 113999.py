n=int(input())
a=list(map(int,input().rstrip().split()))
a.sort()
totalsum=0
for i in range(n):
    sum=0
    for j in range(i+1):
        sum+=a[j]
    totalsum+=sum
print(totalsum)