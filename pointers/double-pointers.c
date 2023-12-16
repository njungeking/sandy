#include<stdio.h>
#include<stdlib.h>

/*The use of double pointers to
display the content of a variable*/

int main()
{
    int a=10,*p=&a,**pp=&p;
    printf("The value of variable 'a' is: %d\n",a);
    printf("The value of pointer 'p' is: %d\n",*p);
    printf("The value of double pointer 'pp' is: %d\n",**pp);
}

