#include<stdio.h>
#include<stdlib.h>

/*Access of the content of a
string using pointers during run-
time initialization*/

int main()
{
    char ask[100],*ptr;
    ptr=ask;
    printf("Welcome to an access program!\n\n");
    printf("Please enter the word/phrase "
           "that you would wish to access: \n\n");
    gets(ask);
    while(*ptr!='\0')
    {
        printf("%c",*ptr);
        *ptr++;
    }
    printf("\n");
}

