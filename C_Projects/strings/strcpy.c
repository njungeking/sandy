#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*Copying the content of one
string into another string using
the strcpy() function and display*/

int main()
{
    char str1[10],str2[10]="Kenya";
    strcpy(str1,str2);
    printf("str1 content is: %s\n",str1);
    printf("str2 content is: %s\n",str2);
}

