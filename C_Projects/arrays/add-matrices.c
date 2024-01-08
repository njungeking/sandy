#include<stdio.h>
#include<stdlib.h>

/*Addition of two 2D-arrays using
run-time initialization and a display
function using matrix format*/

void disp(int a[][100],int m,int n);

int main()
{
    int a[100][100],b[100][100],c[100][100],m,n,i,j;
    printf("Please set the size of the rows and columns of your arrays, respectively: \n");
    scanf("%d%d",&m,&n);
    printf("\nPlease enter %d values as the contents of array 'a': \n",m*n);
    for(i=0;i<m;i++)
    for(j=0;j<n;j++)
    scanf("%d",&a[i][j]);
    printf("\nThe values of array 'a' in a matrix format are: \n\n");
    disp(a,m,n);
    printf("\nPlease enter %d values as the contents of array 'b': \n",m*n);
    for(i=0;i<m;i++)
    for(j=0;j<n;j++)
    scanf("%d",&b[i][j]);
    printf("\nThe values of array 'b' in a matrix format are: \n\n");
    disp(b,m,n);
    for(i=0;i<m;i++)
    for(j=0;j<n;j++)
    c[i][j]=a[i][j]+b[i][j];
    printf("\nThe sum of matrices 'a' and 'b' is: \n\n");
    disp(c,m,n);
}

void disp(int a[][100],int m,int n)
{
    int i,j;
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        printf("%4d",a[i][j]);
        printf("\n\n");
    }
}
