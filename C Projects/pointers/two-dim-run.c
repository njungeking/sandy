#include<stdio.h>
#include<stdlib.h>

/*Accessing the content of a
two-dimensional array using pointers
during run-time initialization*/

int main()
{
    int a[100][100],i,j,m,n;
    printf("Welcome to a 2D array access program!\n\n");
    printf("Please enter the order that you \n"
           "would wish for your matrix: \n\n");
    scanf("%d%d",&m,&n);
    printf("\nPlease enter %d values as the content \n"
           "for your array: \n\n",m*n);
    for(i=0;i<m;i++)
    for(j=0;j<n;j++)
    scanf("%d",*(a+i)+j);
    printf("\nThe values of your array displayed \n"
           "in a matrix format are: \n\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        printf("%4d",*(*(a+i)+j));
        printf("\n\n");
    }
}

