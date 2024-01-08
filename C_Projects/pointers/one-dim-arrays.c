#include<stdio.h>
#include<stdlib.h>

/*Accessing the contents of an
array using pointers during
run-time initialization*/

int main()
{
    int a[100],i,n,*ptr;
    ptr=&a[0];
    printf("Welcome to an array access program!\n\n");
    printf("Please set the size of your array: \n\n");
    scanf("%d",&n);
    printf("\nPlease enter %d values as the content: \n\n",n);
    for(i=0;i<n;i++)
    scanf("%d",ptr+i);
    printf("\nThe content of your array is: \n\n");
    for(i=0;i<n;i++)
    printf("%4d",*(ptr+i));
    printf("\n\n");
}

