#include<stdio.h>
#include<stdlib.h>

/*A review of the sum of numbers using recursion*/

int summation(int x);

int main()
{
    int x,ans;
    printf("Type in the number you wish to get the sum of: \n\n");
    scanf("%d", &x);
    ans=summation(x);
    printf("\nThe sum of number %d is: %d.\n", x,ans);
}

int summation(int x)
{
    int d,sum=0;
    while(x>0)
    {
        d=x%10;
        sum=sum+d;
        x=x/10;
    }
    return sum;
}
