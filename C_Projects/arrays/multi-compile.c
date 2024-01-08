#include<stdio.h>
#include<stdlib.h>

/*A multi-dimensional array using
compile-time initialization and
displaying using a matrix format*/

int main()
{
    int a[2][4][3]={12,2,23,5,40,46,7,6,57,8,
    56,22,4,767,87,787,89,9,32,35,56,67,78,41},i,j,k;
    printf("The values of the two tables of your array are: \n");
    for(i=0;i<2;i++)
    {
        for(j=0;j<4;j++)
        {
            for(k=0;k<3;k++)
            printf("%4d",a[i][j][k]);
            printf("\n");
        }
        printf("\n");
    }
}

