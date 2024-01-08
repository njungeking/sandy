#include<stdio.h>
#include<stdlib.h>

/*Input and display of strings using
gets() and puts() functions respectively,
during run-time initialization*/

int main()
{
    char str[20];
    printf("Please enter your first name: \n\n");
    gets(str);
    printf("\nYour first name is: \n\n");
    puts(str);
}
