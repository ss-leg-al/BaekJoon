#include <stdio.h>

/*int fib(int n)
{
    int r;

    if(n==0)
    r=0;
    else if(n==1)
    r=1;
    else
    r=fib(n-1)+fib(n-2);

    return r;
}
*/
int main(void)
{
    int d,k;
    int a,b;
    int i,j;
    int m=fib(d-2);
    int n=fib(d-1);
 
    


   
   for(i=1;i<k;i++)
    {
     if(((m*i)+(n*j)==k)&&(i<=j))
     break;

     for(j=1;j<k;j++)
     {
        if(((m*i)+(n*j)==k)&&(i<=j))
        {
        a=i;
        b=j;
        break;
        }
     }
    }
    
    printf("%d\n%d",a,b);
    return 0;
    
}