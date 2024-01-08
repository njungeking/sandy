#include<stdio.h>
#include<stdlib.h>

/*Structure pointers*/

struct pets
{
    int petno;
    char name[20];
    float kilo;
};

int main()
{
    struct pets x={23,"Daisy",3.445},*ptr;
    ptr=&x;
    printf("Welcome to a structure-pointers program!\n\n");
    printf("The pet's pet number is: %d.\n\n",ptr->petno);
    printf("The pet's name is: %s.\n\n",ptr->name);
    printf("The pet's weight is: %f.\n\n",ptr->kilo);
}

