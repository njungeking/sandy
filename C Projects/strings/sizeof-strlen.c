#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*Comparing the functionalities
of strlen() and sizeof() coupled with
a display using printf() functions during
run-time initialization*/

int main()
{
    char str[100];
    printf("Please enter any word: \n\n");
    gets(str);
    printf("\nstrlen() functionality gives the value: %d\n\n",strlen(str));
    printf("sizeof() functionality gives the value: %d\n\n",sizeof(str));
}

