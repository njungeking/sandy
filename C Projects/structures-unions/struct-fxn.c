#include<stdio.h>
#include<stdlib.h>

/*Passing of a structure to a
function by passing the address of
a structure variable as the parameter*/

struct digits
{
    int x;
    int y;
};

void disp(struct digits *ptr);

int main()
{
    struct digits p={30,500};
    printf("Welcome to a structure-function program!\n\n");
    disp(&p);
}

void disp(struct digits *ptr)
{
    printf("x=%d\ny=%d\n",ptr->x,ptr->y);
}

