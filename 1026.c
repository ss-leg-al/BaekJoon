#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void)
{
    int *a;
    int *b;
    int *c;
    int n,i,result,pass,tmp;
    int sum=0;

    scanf("%d",&n);
    a=(int*)malloc(sizeof(int)*n);
    b=(int*)malloc(sizeof(int)*n);
    c=(int*)malloc(sizeof(int)*n);

    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }
    for(i=0;i<n;i++)
    {
        scanf("%d",&b[i]);
    }
    
    memcpy(c,b,sizeof(int)*n);

    for(pass=1;pass<n;pass++)
    {
        for(i=0;i<n-1;i++)
        {
            if(a[i]>a[i+1])
            {
            tmp=a[i];
            a[i]=a[i+1];
            a[i+1]=tmp;
            }
        }
    }
    for(pass=1;pass<n;pass++)
    {
        for(i=0;i<n-1;i++)
        {
            if(c[i]<c[i+1])
            {
            tmp=c[i];
            c[i]=c[i+1];
            c[i+1]=tmp;
            }
        }
    }
   
    for(i=0;i<n;i++)
    {
        sum+=(a[i]*c[i]);
    }
   printf("%d",sum);
}