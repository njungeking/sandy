#include<stdio.h>
#include<stdlib.h>

/*Enumerated data types*/

int main()
{
    enum colors{green,yellow,black,brown,red,white};
    enum colors best;
    best=black;
    printf("\n\nThe best color is 'black', which is enum %d.\n\n",best);
}

