#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*Measurement of the length of
a string using strlen() function
during run-time initialization and
display using a printf() function*/

int main()
{
    int len;
    char str[20];
    printf("Please enter your surname: \n\n");
    gets(str);
    len=strlen(str);
    printf("\nYour surname %s, contains: \n\n",str);
    printf("%d characters!\n",len);
}

