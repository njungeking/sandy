#include<stdio.h>
#include<stdlib.h>

/*String concatenation using pointers
and a separate function during run-time
initialization*/

void concat(char *str1,char *str2);

int main()
{
    char s1[100],s2[100];
    printf("Welcome to a string concatenation program!\n\n");
    printf("Please enter the two words that you wish \n"
           "to join together: \n\n");
    gets(s1),gets(s2);
    printf("\nWord 1 before concatenation: %s\n",s1);
    printf("Word 2 before concatenation: %s\n\n",s2);
    concat(s1,s2);
    printf("Word 1 after concatenation: %s\n",s1);
    printf("Word 2 after concatenation: %s\n\n",s2);
}

void concat(char *str1,char *str2)
{
    while(*str1!='\0')
    *str1++;
    while(*str2!='\0')
    *str1++=*str2++;
    *str1='\0';
}

