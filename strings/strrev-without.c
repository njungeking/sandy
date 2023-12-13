#include<stdio.h>
#include<stdlib.h>

/*The reversal of the characters in a
string without the use of strrev()
function but rather iteration during
run-time initialization*/

int main()
{
    char str[100];
    int i,n=0;
    printf("Please enter the word that you \n"
           "would wish to reverse: \n");
    gets(str);
    printf("The reversal of %s gives: \n",str);
    for(i=0;str[i]!='\0';i++)
    n++;
    for(i=n-1;i>=0;i--)
    printf("%c",str[i]);
    printf("\n");
}

