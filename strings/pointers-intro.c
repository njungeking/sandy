#include<stdio.h>
#include<stdlib.h>

/*Switching the contents of two
variables by use of pointers*/

int main()
{
    int a=1000,b=500,*p=&a,*q=&b;
    printf("The content of variable 'a' "
           "before switching: %d\n",*p);
    printf("The content of variable 'b' "
           "before switching: %d\n",*q);
    *p=*p+*q;
    *q=*p-*q;
    *p=*p-*q;
    printf("The content of variable 'a' "
           "after switching: %d\n",*p);
    printf("The content of variable 'b' "
           "after switching: %d\n",*q);
}

