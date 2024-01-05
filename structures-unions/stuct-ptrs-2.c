#include<stdio.h>
#include<stdlib.h>

/*Structures containing pointers*/

struct characters
{
    char c;
    char *cp;
};

int main()
{
    struct characters x;
    char ch='a';
    x.c=ch;
    x.cp=&ch;
    printf("Welcome to a structure containing pointers program!\n\n");
    printf("The character is %c.\n\n",x.c);
    printf("The address of %c is %u.\n\n",x.c,x.cp);
}

