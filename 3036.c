#include <stdio.h>
#include <stdlib.h>
int gcd(int a,int b)
{
    return b?gcd(b,a%b):a;
}
int main(void)
{
    int n;
    int *a;
    int i,j;
    
    scanf("%d",&n);
    a=(int*)malloc(sizeof(int)*n);

    
    for(i=0;i<n;i++)
    {
        scanf("%d",&a[i]);
    }

    for(i=1;i<n;i++)
    {
        printf("%d/%d\n",a[0]/gcd(a[0],a[i]),a[i]/gcd(a[0],a[i]));
    }
   
  
    free(a);
    return 0;

}