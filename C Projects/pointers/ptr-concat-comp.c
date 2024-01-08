#include<stdio.h>
#include<stdlib.h>

/*String concatenation using pointers
during compile-time initialization and
with the use of a separate function*/

void concat(char *str1,char *str2);

int main()
{
    char s1[100]="Africa ",s2[100]="Unite!";
    printf("Welcome to a string concatenation program!\n\n");
    printf("s1 content before concatenation: %s\n\n",s1);
    concat(s1,s2);
    printf("s1 content after concatenation: %s\n\n",s1);
}

void concat(char *str1,char *str2)
{
    while(*str1!='\0')
    *str1++;
    while(*str2!='\0')
    *str1++=*str2++;
    *str1='\0';
}

