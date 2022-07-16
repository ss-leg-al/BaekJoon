import sys
sys.setrecursionlimit(10**6)
a=[]
result=[]
while(1):
    a.append(list(map(int,input().rstrip().split())))
    if a[-1][0]==0:
        a.pop()
        break
def maxarea(s):
    if len(s)==1:
        return s[0]
    if s[0]==0:
        return maxarea(s[1:])
    if s[-1]==0:
        return maxarea(s[:-1])
    center=len(s)//2
    li=center-1
    ri=center
    currentheight=min(s[ri],s[li])
    currentmax=min(s[ri],s[li])*2
    left=s[:center]
    right=s[center:]
    for i in range(len(s)-2):
        if li==0:
            currentheight=min(currentheight,s[ri+1])
            currentmax=max(currentmax,currentheight*(2+i+1))
            ri+=1
        elif ri==len(s)-1:
            currentheight=min(currentheight,s[li-1])
            currentmax=max(currentmax,currentheight*(2+i+1))
            li+=1
        elif s[ri+1]>=s[li-1]:
            currentheight=min(currentheight,s[ri+1])
            currentmax=max(currentmax,currentheight*(2+i+1))
            ri+=1
        else:
            currentheight=min(currentheight,s[li-1])
            currentmax=max(currentmax,currentheight*(2+i+1))
            li-=1
    return max(currentmax,maxarea(left),maxarea(right))
for i in range(len(a)):
    print(maxarea(a[i][1:]))






