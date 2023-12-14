#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*String concatenation using
strcat() during run-time initialization*/

int main()
{
    char s1[100],s2[100];
    printf("Please enter word no.1: \n");
    gets(s1);
    printf("Please enter word no.2: \n");
    gets(s2);
    printf("Word no.1 before concatenation: %s\n",s1);
    printf("Word no.2 before concatenation: %s\n",s2);
    strcat(s1,s2);
    printf("Word no.1 after concatenation: %s\n",s1);
    printf("Word no.2 after concatenation: %s\n",s2);
}

