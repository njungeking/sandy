#include<stdio.h>
#include<stdlib.h>

/*Manipulation of the values in
a variable using pointers during
run-time initialization*/

int main()
{
    int a,*p,**pp;
    p=&a;
    pp=&p;
    printf("Please enter the value you would wish "
           "to work with: \n");
    scanf("%d",&a);
    printf("The value that you chose to work "
           "with is: %d\n",a);
    **pp=a+*p+**pp;
    printf("The result of your choice is: %d\n",a);
    printf("The value of 'a' is: %d\n",a);
    printf("The value of 'p' is: %d\n",*p);
    printf("The value of 'pp' is: %d\n",**pp);
}

