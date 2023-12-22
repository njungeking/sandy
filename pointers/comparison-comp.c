#include<stdio.h>
#include<stdlib.h>

/*String comparison using pointers
during compile-time initialization
and by use of a separate function*/

int comp(char *str1,char *str2);

int main()
{
    char s1[100]="Avid",s2[100]="Technologies";
    int res;
    printf("Welcome to a string comparison program!\n\n");
    res=comp(s1,s2);
    printf("The comparison result of the two strings is: %d!\n\n",res);
}

int comp(char *str1,char *str2)
{
    while((*str1==*str2) && (*str1!=NULL || *str2!=NULL))
    {
        *str1++;
        *str2++;
    }
    return (*str1-*str2);
}

