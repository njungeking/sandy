#include<stdlib.h>
#include<stdlib.h>

/*A final recap on the comparison of
strings using pointers during run-time
initialization and by the use of a
separate function using iteration*/

int comp(char *str1,char *str2);

int main()
{
    char s1[100],s2[100];
    int ans;
    printf("Welcome to a string comparison program!\n\n");
    printf("Please enter the two words that you wish \n"
           "to compare: \n\n");
    gets(s1),gets(s2);
    ans=comp(s1,s2);
    printf("\nThe difference of the two gives the value: %d!\n\n",ans);
}

int comp(char *str1,char *str2)
{
    while((*str1==*str2) && (*str1!=NULL || *str2!=NULL))
    {
        *str1++;
        *str2++;
    }
    return(*str1-*str2);
}

