#include<stdio.h>
#include<stdlib.h>

/*A Multi-Dimensional array using
run-time initialization with a
separate display function*/

void disp(int a[][10][10],int m,int n,int o);

int main()
{
    int a[10][10][10],m,n,o,i,j,k;
    printf("Please set the size of the tables,\n"
           "rows and columns for your Multi-Dimensional\n"
           "array: \n\n");
    scanf("%d%d%d",&m,&n,&o);
    printf("\nPlease enter %d values as the contents of your array: \n\n",m*n*o);
    for(i=0;i<m;i++)
    for(j=0;j<n;j++)
    for(k=0;k<o;k++)
    scanf("%d",&a[i][j][k]);
    disp(a,m,n,o);
}

void disp(int a[][10][10],int m,int n,int o)
{
    int i,j,k;
    printf("\nThe values of your Multi-Dimensional array\n"
           "displayed in a matrix format are: \n\n");
    for(i=0;i<m;i++)
    {
        for(j=0;j<n;j++)
        {
            for(k=0;k<o;k++)
            printf("%4d",a[i][j][k]);
            printf("\n");
        }
        printf("\n");
    }
}

