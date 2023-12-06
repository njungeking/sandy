#include<stdio.h>
#include<stdlib.h>

/*A two-dimensional array using run-time
initialization and a display function plus
a transposition function both in a matrix
format*/

void disp(int a[][100],int m,int n);

void transpose(int a[][100],int m,int n);

int main()
{
    int a[100][100],m,n,i,j;
    printf("Please set the size of the rows and columns your array: \n");
    scanf("%d%d",&m,&n);
    printf("Please enter %d values for your array: \n",m*n);
    for(i=0;i<m;i++)
    for(j=0;j<n;j++)
    scanf("%d",&a[i][j]);
    disp(a,m,n);
    transpose(a,m,n);
}

void disp(int a[][100],int m,int n)
{
    int i,j;
    printf("The values of your array in a matrix format are: \n\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        printf("%4d",a[i][j]);
        printf("\n\n");
    }
}

void transpose(int a[][100],int m,int n)
{
    int i,j;
    printf("Transposed version of the values of the matrix are: \n\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        printf("%4d",a[j][i]);
        printf("\n\n");
    }
}
