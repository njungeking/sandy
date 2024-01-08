#include<stdio.h>
#include<stdlib.h>

/*Pointer arithmetic involving
increment of the memory location
of integers*/

int main()
{
    int a,*p;
    a=10;
    p=&a;
    printf("The address of pointer '*p' before "
           "incrementing is: %u\n",p);
    p=p+2;
    printf("The address of pointer '*p' after "
           "incrementing is: %u\n",p);
}

