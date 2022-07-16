#include <stdio.h>

int ispalin(int a)
{
    int k;
    int r=0;
    k=a;
    while(k>0)
    {
        r=(r*10)+(k%10);
        k=k/10;
    }
    if(a==r)
    return 1;
    else 
    return 0;
}
int main(void)
{
    int n;
    scanf("%d",&n);
    while(1)
   {
       n++;
       if(ispalin(n))
       break;
   }
   printf("%d",n);
}