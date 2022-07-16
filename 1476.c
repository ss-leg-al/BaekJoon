#include<stdio.h>

int main(void)
{
    int e,s,m;
    int a=0,b=0,c=0;
    int count;

    scanf("%d %d %d",&e,&s,&m);

    for(count=0;;a++,b++,c++)
    {
        
        
        if(a>15)
        a=1;
        if(b>28)
        b=1;
        if(c>19)
        c=1;

        if((a==e)&&(b==s)&&(c==m))
        break;
        count++;

    }
    printf("%d\n",count);
    return 0;

}