#include<stdio.h>
#include<stdlib.h>

/*A review on Fibonacci using recursion*/

int fibo(int x);

int main()
{
    int x,ans;
    printf("Please type in a number for the Fibonacci value: \n\n");
    scanf("%d", &x);
    ans=fibo(x);
    printf("\nThe fibonacci value of %d is: %d.\n", x,ans);
}

int fibo(int x)
{
    if(x==1)
    return 0;
    else if(x==2)
    return 1;
    else
    return fibo(x-1)+fibo(x-2);
}
