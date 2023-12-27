#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

/*Memory allocation using the malloc
functionality and de-allocation using
the free() functionality while applying
pointers*/

int main()
{
    int *ptr,i,n;
    printf("Welcome to a memory allocation program!\n\n");
    printf("Please enter the size that you wish to allocate: \n\n");
    scanf("%d",&n);
    ptr=(int*)malloc(n*sizeof(int));
    printf("\nPlease enter %d values for allocation: \n\n",n);
    for(i=0;i<n;i++)
    scanf("%d",ptr+i);
    printf("\nThe values that have been stored are: \n\n");
    for(i=0;i<n;i++)
    printf("%4d",*(ptr+i));
    printf("\n\n");
    free(ptr);
}

