#include<stdio.h>
#include<stdlib.h>

/*Switching of the contents of
two variables using pointers
during run-time initialization*/

int main()
{
    int a,b,*p=&a,*q=&b;
    printf("Welcome to a value switching program!\n\n");
    printf("Please enter the first value: \n");
    scanf("%d",&a);
    printf("Please enter the second value: \n");
    scanf("%d",&b);
    printf("The first value before switching is: %d\n",*p);
    printf("The second value before switching is: %d\n",*q);
    *p=*p+*q;
    *q=*p-*q;
    *p=*p-*q;
    printf("The first value after switching is: %d\n",*p);
    printf("The second value after switching is: %d\n",*q);
}

