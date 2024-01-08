#include<stdio.h>
#include<stdlib.h>

/*Reference to functions using
pointers during run-time initialization*/

int summation();

int main()
{
    int result,(*p)();
    p=&summation;
    printf("Welcome to a summation program!\n\n");
    result=(*p)();
    printf("\nThe final result is: %d\n",result);
}

int summation()
{
    int a,b,c;
    printf("Please enter the three values that you "
           "would wish to add: \n\n");
    scanf("%d%d%d",&a,&b,&c);
    return a+b+c;
}

