#include <stdio.h>
#include <string.h>
int time(n)
{
    switch(n)
    {
        case 'A':
        case 'B':
        case 'C':
        return 3;

        case 'D':
        case 'E':
        case 'F':
        return 4;

        case 'G':
        case 'H':
        case 'I':
        return 5;

        case 'J':
        case 'K':
        case 'L':
        return 6;

        case 'M':
        case 'N':
        case 'O':
        return 7;

        case 'P':
        case 'Q':
        case 'R':
        case 'S':
        return 8;

        case 'T':
        case 'U':
        case 'V':
        return 9;

        default:
        return 10;
    }
}
int main(void)
{
    char a[15]={0};
    int i,j;
    int sum=0;
    scanf("%s",a);

    for(i='A';i<='Z';i++)
    {
        for(j=0;j<strlen(a);j++)
    {
        if(i==a[j])
        sum+=time(i);
    }
    }
    printf("%d",sum);
    return 0;

}