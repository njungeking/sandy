#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*The reversal of the characters in a
string using the strrev() function
during run-time initialization*/

int main()
{
    char str[100];
    printf("Please type the word that you \n"
           "wish to reverse: \n");
    gets(str);
    printf("\nThe reverse of: %s is: \n",str);
    strrev(str);
    puts(str);
}

