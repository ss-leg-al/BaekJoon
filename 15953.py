n=int(input())
list=[]
def first(rank):
    if rank==1:
        return 5000000
    elif 1<rank<4:
        return 3000000
    elif 3<rank<7:
        return 2000000
    elif 6<rank<11:
        return 500000
    elif 10<rank<16:
        return 300000
    elif 15<rank<22:
        return 100000
    else:
        return 0
def second(rank):
    if rank==1:
        return 5120000
    elif 1<rank<4:
        return 2560000
    elif 3<rank<8:
        return 1280000
    elif 7<rank<16:
        return 640000
    elif 15<rank<32:
        return 320000
    else:
        return 0
for i in range(n):
    firstR,secondR=map(int,input().split())
    list.append(first(firstR)+second(secondR))
for i in list:
    print(i)