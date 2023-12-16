#include<stdio.h>
#include<stdlib.h>

/*The manipulation of the contents
of a variable(memory location)
using double pointers*/

int main()
{
    int a,*p,**pp;
    a=100;
    p=&a;
    pp=&p;
    printf("Welcome to a double pointers program!\n\n");
    printf("The value of 'a' before manipulation: %d\n",a);
    printf("The value of '*p' before manipulation: %d\n",*p);
    printf("The value of '**pp' before manipulation: %d\n",**pp);
    printf("\n\n");
    **pp=*p+a+*p;
    printf("The value of 'a' after manipulation: %d\n",a);
    printf("The value of '*p' after manipulation: %d\n",*p);
    printf("The value of '**p' after manipulation: %d\n",**pp);
    printf("\n\n");
}

