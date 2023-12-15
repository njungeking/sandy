#include<stdio.h>
#include<stdlib.h>

/*String concatenation during
run-time initialization using
iteration*/

int main()
{
    int i,j;
    char s1[100],s2[100];
    printf("Please input word no.1: \n");
    gets(s1);
    printf("Please input word no.2: \n");
    gets(s2);
    printf("Word no.1 before concatenation: %s\n",s1);
    printf("Word no.2 before concatenation: %s\n",s2);
    for(i=0;s1[i]!='\0';i++);
    for(j=0;s2[j]!='\0';j++)
    {
        s1[i]=s2[j];
        i++;
    }
    s1[i]='\0';
    printf("s1 content after concatenation: %s\n",s1);
    printf("s2 content after concatenation: %s\n",s2);
}

