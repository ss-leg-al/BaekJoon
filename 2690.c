#include <stdio.h>
int n(int a,int b)
{
    return (b?n(b,a%b):a);
}
int m(int a, int b)
{
    return n(a,b)*(a/n(a,b))*(b/(n(a,b)));
}




int main(void)
{
    int a,b;
    scanf("%d %d",&a,&b);
    printf("%d\n%d",n(a,b),m(a,b));
}