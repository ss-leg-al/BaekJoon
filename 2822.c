#include <stdio.h>
#include <string.h>
int main(void)
{
    int a[8];
    int i,j;
    int tmp;
    int pass;
    int b[8];
    int sum=0;
    for(i=0;i<8;i++)
    {
        scanf("%d",&a[i]);
    }
   

    memcpy(b,a,sizeof(int)*8);
     for(pass=1;pass<8;pass++)
    {
        for(i=0;i<7;i++)
        {
            if(b[i]<b[i+1])
            {
            tmp=b[i];
            b[i]=b[i+1];
            b[i+1]=tmp;
            }
        }
    }
    for(i=0;i<5;i++)
    sum+=b[i];
    printf("%d\n",sum);
    for(i=0;i<8;i++)
    for(j=0;j<5;j++)
    if(a[i]==b[j])
    printf("%d ",i+1);

    return 0;

}