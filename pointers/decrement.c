#include<stdio.h>
#include<stdlib.h>

/*Pointer arithmetic involving the
decrement of the memory location
of integers*/

int main()
{
    int a,*p;
    a=100;
    p=&a;
    printf("The address of '*p', before "
           "decrement: %u\n",p);
    p=p-3;
    printf("The address of '*p', after "
           "decrement: %u\n",p);
}

