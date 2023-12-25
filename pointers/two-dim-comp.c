#include<stdio.h>
#include<stdlib.h>

/*Accessing the content of a 2D
array using pointers during compile-
time initialization*/

int main()
{
    int arr[3][3]={1,2,3,4,5,6,7,8,9},i,j;
    printf("Welcome to a 2D array access program!\n\n");
    printf("The values of your array displayed in \n"
           "a matrix format are: \n\n");
    for(i=0;i<3;i++)
    {
        for(j=0;j<3;j++)
        printf("%4d",*(*(arr+i)+j));
        printf("\n\n");
    }
}

