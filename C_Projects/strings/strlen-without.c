#include<stdio.h>
#include<stdlib.h>

/*Measurement of the length of a
string without the use of strlen()
function and final display using
printf() function*/

int main()
{
    int len=0,i;
    char str[20];
    printf("Please enter your Surname: \n\n");
    gets(str);
    for(i=0;str[i]!='\0';i++)
    len++;
    printf("\nYour Surname; %s, contains: \n\n",str);
    printf("%d characters!\n\n",len);
}

