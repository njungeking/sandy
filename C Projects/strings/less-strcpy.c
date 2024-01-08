#include<stdio.h>
#include<stdlib.h>

/*Copying of the content of one
string into another string without
the use of strcpy() function but rather
iteration*/

int main()
{
    char str1[10],str2[]="Kenya";
    int i;
    for(i=0;str2[i]!='\0';i++)
    str1[i]=str2[i];
    str1[i]='\0';
    printf("str1 content is: %s\n",str1);
    printf("str2 content is: %s\n",str2);
}

