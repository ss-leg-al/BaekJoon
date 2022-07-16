#include <stdio.h>
#include <stdlib.h>

int p(int n)
{
    int r=0;
    int i;
    int count=0;
    for(i=1;i<=n/2;i++)
    {
        if((n%i)==0)
        count++;
    }
    if(count==2)
    r=1;

    return r;
}
int up(int n)
{
   int i;
   for(i=0;;i++)
   {
       if(p(n+i)==1)
       break;
   }
   return n+i;

}
int dp(int n)
{
    int i;
   for(i=0;;i++)
   {
       if(p(n-i)==1)
       break;
   }
   return n-i;

}
int main(void)
{
    int *a;
    int t;
    int i;
    scanf("%d",&t);
    a=(int*)malloc(sizeof(int)*t);
    for(i=0;i<t;i++)
    scanf("%d",&a[i]);

    for(i=0;i<t;i++)
    {
        if(p(a[i])!=1)
        printf("%d\n",up(a[i])-dp(a[i]));
        else
        printf("0\n");
    }
    return 0;

}
