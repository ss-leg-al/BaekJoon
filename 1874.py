l=[]
pp=[]
n=int(input())
count=1
r=True

for i in range(n):
    num=int(input())
    while count<=num:
        l.append(count)
        pp.append('+')
        count+=1
    if l[-1]==num:
        l.pop()
        pp.append('-')
    else:
        r=False
if r==False:
    print('NO')
else:
    for i in pp:
        print(i)


        
    
    




