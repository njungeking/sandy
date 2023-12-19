#include<stdio.h>
#include<stdlib.h>

/*Finding the length of a
string using pointers during
run-time initialization through
iteration*/

int main()
{
    char str[100],*ptr;
    ptr=str;
    int len=0;
    printf("Welcome to a character counting program!\n\n");
    printf("Please enter the word/phrase that you would \n"
           "wish to get the length of: \n\n");
    gets(str);
    while(*ptr!='\0')
    {
        *ptr++;
        len++;
    }
    printf("\nThe length of (%s) is: %d!\n\n",str,len);
}

