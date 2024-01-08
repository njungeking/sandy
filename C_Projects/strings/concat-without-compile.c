#include<stdio.h>
#include<stdlib.h>

/*string concatenation using
iteration during compile-time
initialization*/

int main()
{
    char s1[100]="Hello ",s2[100]="World";
    int i,j;
    printf("s1 content before concatenation: %s\n",s1);
    printf("s2 content before concatenation: %s\n",s2);
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

