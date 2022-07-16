#include <stdio.h>
/*#include <stdlib.h>

int main(void)
{
    int l,p,v;
    int *varray;
    int i,j;
    int count;
    while(l!=0&&p!=0&&v!=0)
    {
        scanf("%d %d %d",l,p,v);
        varray=(int*)malloc(sizeof(int)*v);
        for(i=0;i<v;i++)
        varray[i]=1;
       
        for(i=0;i<v-p+2;i++)
        {
             for(j=0;j<p;j++)
             {
                 if(varray==1)
                 count++;


             }
         

         
          }

        
        



    
    }

}*/
int main(void)
{
    int l,p,v;
    int r;
    int k;
    int count=1;

    while(1)
    {
    scanf("%d %d %d",&l,&p,&v);
    if(l==0&&p==0&&v==0)
    break;
    if((v%p)<=l)
    k=(v%p);
    else
    k=l;

    r=((v/p)*l)+k;
    printf("Case %d: %d\n",count,r);
    count++;

    }
    return 0;
}
