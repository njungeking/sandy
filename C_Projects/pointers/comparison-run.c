#include<stdio.h>
#include<stdlib.h>

/*String comparison using pointers
during run-time initialization and
by the use of a separate function*/

int comp(char *str1,char *str2);

int main()
{
    char s1[100],s2[100];
    int res;
    printf("Welcome to a string comparison program!\n\n");
    printf("Please enter the two words that \n"
           "you would wish to compare: \n\n");
    gets(s1),gets(s2);
    res=comp(s1,s2);
    printf("\nThe comparison result is: %d!\n\n",res);
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

