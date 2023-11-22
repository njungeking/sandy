#include<stdio.h>
#include<stdlib.h>

/*A review on factorial using functions*/

int fact(int x);

int main()
{
    int x,ans;
    printf("Please type in the number you wish to get the factorial of: \n\n");
    scanf("%d",&x);
    ans=fact(x);
    printf("\nThe factorial of %d is: %d.\n",x,ans);
}

int fact(x)
{
    int i,f=1;
    for(i=1;i<=x;i++)
    f=f*i;
    return f;
}
