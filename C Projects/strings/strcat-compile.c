#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*The concatenation of two strings
using strcat() function during
compile-time initialization*/

int main()
{
    char s1[]="Hello",s2[]="Enola";
    printf("s1 content before concatenation: %s\n",s1);
    printf("s2 content before concatenation: %s\n",s2);
    strcat(s1,s2);
    printf("s1 content after concatenation: %s\n",s1);
    printf("s2 content after concatenation: %s\n",s2);
}

