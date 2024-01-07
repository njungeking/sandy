#include<stdio.h>
#include<stdlib.h>

/*Unions*/

union digits
{
    int x;
    int y;
};

int main()
{
    union digits x;
    printf("welcome to a Unions program!\n\n");
    x.x=100;
    printf("The first value is, x=%d.\n\n",x.x);
    x.y=500;
    printf("The second value is, y=%d.\n\n",x.y);
}

