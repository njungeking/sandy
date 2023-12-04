#include<stdio.h>
#include<stdlib.h>

/*A two-dimensional array using
compile-time initialization and
display in a matrix format*/

int main()
{
    int a[4][6]={12,43,23,65,23,76,54,32,65,432,54,664},i,j;
    printf("The values of your array are: \n\n");
    for(i=0;i<4;i++)
    {
        for(j=0;j<6;j++)
        printf("%4d",a[i][j]);
        printf("\n\n");
    }
}`
