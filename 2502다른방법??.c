#include <stdio.h>

int fib(int n)
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
int main(void)
{
    int d,k;
    int a=1,b=1;
    int m=fib(d-2);
    int n=fib(d-1);
    int sum=1;
    
    
    scanf("%d %d",&d,&k);
    while (1) 
    {
        sum = 0;
        sum += m * a;
        b = 1;
        while (1) {
            sum += n * b;
            if (sum > k) break;
 
            if (sum == k) {
                printf("%d\n", a);
                printf("%d\n", b);
                return 0;
            }
            sum -= n * b;
            b++;
        }
        b++;
        
    }
    return 0;
}