#include<stdio.h>
#include<stdlib.h>

/*Finding the length of a string
using pointers during run-time
initialization and passing the
string as a parameter to a separate function*/

int len(char *ptr);

int main()
{
    char str[100];
    int ans;
    printf("Welcome to a length finding operation!\n\n");
    printf("Please enter the word/phrase that \n"
           "you would like to get the length of: \n\n");
    gets(str);
    ans=len(str);
    printf("\nThe length of (%s) is: %d characters!\n\n",str,ans);
}

int len(char *ptr)
{
    char *temp;
    temp=ptr;
    while(*temp!='\0')
    *temp++;

    return(temp-ptr);
}

