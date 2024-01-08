#include<stdio.h>
#include<stdlib.h>

/*Yet another recap of passing a
structure to a function by using
the address to the structure as the
parameter*/

struct numbers
{
    int x;
    int y;
};

void disp(struct numbers *ptr);

int main()
{
    struct numbers x={100,800};
    printf("Welcome to a structure function program!\n\n");
    disp(&x);
}

void disp(struct numbers *ptr)
{
    printf("The values are: \n\n");
    printf("x=%d\ny=%d\n\n",ptr->x,ptr->y);
}

