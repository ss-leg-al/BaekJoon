#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int p(int n)
{
    int r=0;
    int i;
    int count=0;
    for(i=1;i<=n;i++)
    {
        if((n%i)==0)
        count++;
    }
    if(count==2)
    r=1;

    return r;
}
int main(void)
{
    int k;
    int n;
    int i,j;
    int count=0;
    scanf("%d",&n);
    
    for(i=0,k=0;i<pow(10,n)-pow(10,n-1)-1;i++)
    {   
     count=0;
     k=pow(10,n-1)+i;
     for(j=0;j<n;j++)
     {
         if(p(k/pow(10,j))==1)
         count++;
     }
     if(count==4)
     printf("%d\n",k);

    }
    
    return 0;

}
