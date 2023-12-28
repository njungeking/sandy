#include<stdio.h>
#include<stdlib.h>
#include<malloc.h>

/*Memory block allocation using malloc
functionality and de-allocation using
free() functionality during run-time
initialization*/

int main()
{
    int i,n,*ptr;
    printf("Welcome to a memory block allocation program!\n\n");
    printf("Please enter the size that you wish to allocate \n"
           "your array: \n\n");
    scanf("%d",&n);
    ptr=(int*)calloc(n,sizeof(int));
    printf("\nPlease enter %d values for your array: \n\n",n);
    for(i=0;i<n;i++)
    scanf("%d",ptr+i);
    printf("\nThe values of your array are: \n\n");
    for(i=0;i<n;i++)
    printf("%4d",*(ptr+i));
    printf("\n\n");
    free(ptr);
}

