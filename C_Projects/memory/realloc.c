#include<stdio.h>
#include<stdlib.h>
#include<string.h>
#include<malloc.h>

/*Memory re-allocation during
compile-time initialization*/

int main()
{
    char *ptr;
    ptr=(char*)malloc(20*sizeof(char));
    strcpy(ptr,"Happy");
    printf("Before re-allocation: \n"
           "%s. The address is: %p\n\n",ptr,ptr);
    ptr=(char*)realloc(ptr,40);
    strcpy(ptr,"Happy New Year!");
    printf("After re-allocation: \n"
           "%s. The address is: %p\n\n",ptr,ptr);
    free(ptr);
}

