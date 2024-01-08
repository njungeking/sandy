#include<stdio.h>
#include<stdlib.h>

/*Another recap on the use of pointers
to concatenate two strings during run-time
initialization using a separate function*/

void concat(char *str1,char *str2);

int main()
{
    char s1[100],s2[100];
    printf("Welcome to a string concatenation program!\n\n");
    printf("Please enter the two words that you \n"
           "wish to concatenate: \n\n");
    gets(s1),gets(s2);
    concat(s1,s2);
    printf("\nThe final conjoined result is: %s!\n\n",s1);
}

void concat(char *str1,char *str2)
{
    while(*str1!=NULL)
    *str1++;
    while(*str2!=NULL)
    {
        *str1++=*str2++;
        *str1=NULL;
    }
}

