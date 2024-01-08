#include<stdio.h>
#include<stdlib.h>
#include<string.h>

/*Structures syntax initialization*/

struct pupils
{
    int sno;
    char name[30];
    float marks;
};

int main()
{
    struct pupils x;
    x.sno=23;
    strcpy(x.name,"Paulie");
    x.marks=99;
    printf("Welcome to a structers program!\n\n");
    printf("Pupil registration number: %d\n\n",x.sno);
    printf("Pupil name: %s\n\n",x.name);
    printf("Pupil marks: %f\n\n",x.marks);
}

