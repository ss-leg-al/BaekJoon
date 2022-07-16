#include <stdio.h>

int gcd(int a,int b)
{
    int r;
    r=(b?gcd(b,a%b):a);
    return r;
}
int main(void)
{
    int n,m;
    int r;
    scanf("%d %d",&n,&m);
    r=((m/gcd(n,m))-1)*gcd(n,m);
    printf("%d",r);
    return 0;
}
